from common.exceptions import ValidationException
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from itinerary.models.day import Day
from itinerary.models.itinerary import Itinerary
from itinerary.serializers.day import DaySerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        itinerary_id = self.kwargs.get("itinerary_id")
        return (
            super()
            .get_queryset()
            .filter(owner=self.request.user, itinerary__id=itinerary_id)
        )

    def perform_create(self, serializer):
        itinerary_id = self.kwargs.get("itinerary_id")
        serializer.save(itinerary_id=itinerary_id)


class MoveDayView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, itinerary_id):
        method = request.data.get("method", "")
        day = Day.objects.filter(owner=request.user, itinerary__id=itinerary_id)
        if method == "up":
            day.up()
        elif method == "down":
            day.down()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
