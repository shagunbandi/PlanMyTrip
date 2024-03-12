from common.exceptions import ValidationException
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from itinerary.models.agenda import Agenda
from itinerary.models.itinerary import Itinerary
from itinerary.models.place import Place
from itinerary.serializers.place import PlaceSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        itinerary_id = self.kwargs.get("itinerary_id")
        agenda_id = self.kwargs.get("agenda_id")

        return (
            super()
            .get_queryset()
            .filter(
                owner=self.request.user,
                agenda__id=agenda_id,
                agenda__itinerary__id=itinerary_id,
            )
        )

    def perform_create(self, serializer):
        itinerary_id = self.kwargs.get("itinerary_id")
        agenda_id = self.kwargs.get("agenda_id")

        agenda = Agenda.objects.filter(
            owner=self.request.user, id=agenda_id, itinerary__id=itinerary_id
        )
        if agenda.exists():
            serializer.save(agenda_id=agenda_id)
        else:
            raise ValueError("Agenda does not exist")


class MovePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, itinerary_id, agenda_id, place_id):
        method = request.data.get("method", "")
        current_place = get_object_or_404(
            Place,
            owner=request.user,
            id=place_id,
            agenda__id=agenda_id,
            agenda__itinerary__id=itinerary_id,
        )

        if method == "up":
            previous_place = current_place.previous()
            if (
                previous_place is None
                or previous_place.agenda.id is not current_place.agenda.id
            ):
                previous_agenda = current_place.agenda.previous()
                if previous_agenda is None:
                    raise ValidationException("Cannot move up")
                current_place.agenda = previous_agenda
                current_place.save()
            current_place.up()

        elif method == "down":
            next_place = current_place.next()
            if (
                next_place is None
                or next_place.agenda.id is not current_place.agenda.id
            ):
                next_agenda = current_place.agenda.next()
                if next_agenda is None:
                    raise ValidationException("Cannot move down")
                current_place.agenda = next_agenda
                current_place.save()
            current_place.down()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
