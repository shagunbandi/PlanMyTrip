from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Dish
from .serializers import create_dish_serializer


class DishViewSet(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        day_id = self.request.GET.get("day_id", None)
        return Dish.objects.filter(user=user, day__id=day_id)

    def get_serializer_class(self):
        day_id = self.request.GET.get("day_id", None)
        return create_dish_serializer(day_id=day_id, user=self.request.user)
