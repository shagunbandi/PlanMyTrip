from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Day
from .serializers import DaySerializer, create_day_serializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        itinerary_id = self.request.GET.get("itinerary_id", None)
        return Day.objects.filter(user=user, itinerary__id=itinerary_id)

    def get_serializer_class(self):
        itinerary_id = self.request.GET.get("itinerary_id", None)
        return create_day_serializer(itinerary_id=itinerary_id)
