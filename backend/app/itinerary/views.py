from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

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
