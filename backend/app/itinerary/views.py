from common.exceptions import ValidationException
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Day, Itinerary, Places
from .serializers import DaySerializer, ItinerarySerializer, PlaceSerializer


class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        itinerary = self._get_itinerary()
        return (
            super().get_queryset().filter(owner=self.request.user, itinerary=itinerary)
        )

    def perform_create(self, serializer):
        itinerary = self._get_itinerary()

        serializer.save(itinerary=itinerary)

    def _get_itinerary(self):
        itinerary_id = self.kwargs.get("itinerary_id")
        itinerary = get_object_or_404(
            Itinerary, pk=itinerary_id, owner=self.request.user
        )
        return itinerary


class PlacesViewSet(viewsets.ModelViewSet):
    queryset = Places.objects.all()
    serializer_class = PlaceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)

    def _get_itinerary(self):
        itinerary_id = self.kwargs.get("itinerary_id")
        itinerary = get_object_or_404(
            Itinerary, pk=itinerary_id, owner=self.request.user
        )
        return itinerary


class MovePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, content_type, object_id, method):
        if content_type not in ["day", "place"]:
            raise ValidationException("Invalid content type.")
        model_class = (
            ContentType.objects.filter(model=content_type.lower()).first().model_class()
        )
        model_object = get_object_or_404(model_class, id=object_id, owner=request.user)

        if method == "up":
            model_object.up()
        elif method == "down":
            model_object.down()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
