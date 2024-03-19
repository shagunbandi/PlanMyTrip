from common.exceptions import ValidationException
from django.db.transaction import atomic
from django.shortcuts import get_object_or_404
from plan.models.agenda import Agenda
from plan.models.place import Place
from plan.serializers.place import PlaceSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        plan_id = self.kwargs.get("plan_id")
        agenda_id = self.kwargs.get("agenda_id")

        return (
            super()
            .get_queryset()
            .filter(
                owner=self.request.user,
                agenda__id=agenda_id,
                agenda__plan__id=plan_id,
            )
        )

    def perform_create(self, serializer):
        plan_id = self.kwargs.get("plan_id")
        agenda_id = self.kwargs.get("agenda_id")

        agenda = Agenda.objects.filter(
            owner=self.request.user, id=agenda_id, plan__id=plan_id
        )
        if agenda.exists():
            serializer.save(agenda_id=agenda_id)
        else:
            raise ValueError("Agenda does not exist")


class MovePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, plan_id, agenda_id, place_id):
        method = request.data.get("method", "")
        current_place = get_object_or_404(
            Place,
            owner=request.user,
            id=place_id,
            agenda__id=agenda_id,
            agenda__plan__id=plan_id,
        )

        if method == "up":
            self._move_up(current_place)
        elif method == "down":
            self._move_down(current_place)
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)

    def _move_down(self, current_place):
        next_place = current_place.next()
        if next_place is not None:
            current_place.down()
        else:
            next_agenda = current_place.agenda.next()
            if next_agenda is None:
                raise ValidationException("Cannot move up")
            current_place.agenda = next_agenda
            with atomic():
                current_place.save()
                current_place.top()

    def _move_up(self, current_place):
        previous_place = current_place.previous()
        if previous_place is not None:
            current_place.up()
        else:
            previous_agenda = current_place.agenda.previous()
            if previous_agenda is None:
                raise ValidationException("Cannot move up")
            current_place.agenda = previous_agenda
            current_place.save()
