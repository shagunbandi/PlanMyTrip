from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Attraction
from .serializers import create_attraction_serializer


class AttractionViewSet(viewsets.ModelViewSet):
    queryset = Attraction.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        day_id = self.request.GET.get("day_id", None)
        return Attraction.objects.filter(user=user, day__id=day_id)

    def get_serializer_class(self):
        day_id = self.request.GET.get("day_id", None)
        return create_attraction_serializer(day_id=day_id, user=self.request.user)
