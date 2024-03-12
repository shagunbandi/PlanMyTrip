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
        place = get_object_or_404(
            Place,
            owner=request.user,
            id=place_id,
            agenda__id=agenda_id,
            itinerary__id=itinerary_id,
        )

        if method == "up":
            previous_place = place.previous()
            if (
                previous_place is not None
                and previous_place.agenda.id is not place.agenda.id
            ):
                place.agenda = previous_place.agenda
            place.up()
        elif method == "down":
            next_place = place.next()
            if next_place is not None and next_place.agenda.id is not place.agenda.id:
                place.agenda = next_place.agenda
            place.down()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
