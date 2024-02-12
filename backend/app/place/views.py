from common.permissions.IsOwner import IsOwner
from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Place
from .serializers import PlaceSerializer


class PlaceViewSet(viewsets.ModelViewSet):
    queryset = Place.objects.all()
    permission_classes = [IsAuthenticated, IsOwner]
    serializer_class = PlaceSerializer


class MovePlaceView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, itinerary_id, day_id, place_id, method):
        user = request.user
        place = get_object_or_404(Place, id=place_id, day__id=day_id, user=user)

        if method == "up":
            place.up()
        elif method == "down":
            place.down()
        else:
            return Response(
                {"detail": "Invalid method parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
