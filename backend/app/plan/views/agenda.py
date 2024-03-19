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
            serializer.save(plan_id=plan_id)
        else:
            raise ValueError("Plan does not exist")


class MoveAgendaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, plan_id, agenda_id):
        method = request.data.get("method", "")
        agenda = get_object_or_404(
            Agenda, owner=request.user, id=agenda_id, plan__id=plan_id
        )
        if method == "up":
            agenda.up()
        elif method == "down":
            agenda.down()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
