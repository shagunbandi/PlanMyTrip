from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Restaurant
from .serializers import create_restaurant_serializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        day_id = self.request.GET.get("day_id", None)
        return Restaurant.objects.filter(user=user, day__id=day_id)

    def get_serializer_class(self):
        day_id = self.request.GET.get("day_id", None)
        return create_restaurant_serializer(day_id=day_id, user=self.request.user)
