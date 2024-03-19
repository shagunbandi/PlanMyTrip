from common.exceptions import ValidationException
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from plan.models.agenda import Agenda
from plan.models.plan import Plan
from plan.serializers.agenda import AgendaSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        plan_id = self.kwargs.get("plan_id")
        return super().get_queryset().filter(owner=self.request.user, plan__id=plan_id)

    def perform_create(self, serializer):
        plan_id = self.kwargs.get("plan_id")
        plan = Plan.objects.filter(owner=self.request.user, id=plan_id)
        if plan.exists():
            agenda = serializer.save(plan_id=plan_id)
            if not agenda.is_itinerary:
                list_count = Agenda.objects.filter(
                    plan_id=plan_id, is_itinerary=False
                ).count()
                new_agenda_index = list_count - 1
                agenda.to(new_agenda_index)
        else:
            raise ValueError("Plan does not exist")


class MoveAgendaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, plan_id, agenda_id):
        method = request.data.get("method", "")
        agenda = get_object_or_404(
            Agenda, owner=request.user, id=agenda_id, plan__id=plan_id
        )

        # Moving UP
        if method == "up":
            if agenda.order == 0:
                if agenda.is_itinerary:
                    agenda.is_itinerary = False
                    agenda.save()
                else:
                    raise ValidationException("Cannot move agena up")
            elif agenda.is_itinerary:
                previous_agenda = agenda.previous()
                if previous_agenda.is_itinerary:
                    agenda.up()
                else:
                    agenda.is_itinerary = False
                    agenda.save()
            else:
                agenda.up()

        # Moving Down
        elif method == "down":
            max_order = Agenda.objects.filter(plan_id=plan_id).count() - 1
            if agenda.order == max_order:
                if not agenda.is_itinerary:
                    agenda.is_itinerary = True
                    agenda.save()
                else:
                    raise ValidationException("Cannot move agenda down")
            elif not agenda.is_itinerary:
                next_agenda = agenda.next()
                if not next_agenda.is_itinerary:
                    agenda.down()
                else:
                    agenda.is_itinerary = True
                    agenda.save()
            else:
                agenda.down()

        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
