from itinerary.models.itinerary import Itinerary
from itinerary.serializers.itinerary import ItinerarySerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)
