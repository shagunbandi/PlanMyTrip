from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Restaurant
from .serializers import create_restaurant_serializer


class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        day_id = self.kwargs.get("day_id", None)
        return Restaurant.objects.filter(user=user, day__id=day_id)

    def get_serializer_class(self):
        day_id = self.kwargs.get("day_id", None)
        return create_restaurant_serializer(day_id=day_id, user=self.request.user)


class MoveRestaurantView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, itinerary_id, day_id, restaurant_id, method):
        user = request.user
        restaurant = get_object_or_404(
            Restaurant, id=restaurant_id, day__id=day_id, user=user
        )

        if method == "up":
            restaurant.up()
        elif method == "down":
            restaurant.down()
        else:
            return Response(
                {"detail": "Invalid method parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
