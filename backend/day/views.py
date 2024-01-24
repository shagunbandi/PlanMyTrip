from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Day
from .serializers import DaySerializer, create_day_serializer


class DayViewSet(viewsets.ModelViewSet):
    queryset = Day.objects.all()
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Customize the queryset based on the authenticated user
        user = self.request.user
        itinerary_id = self.request.GET.get("itinerary_id", None)
        return Day.objects.filter(user=user, itinerary__id=itinerary_id)

    def get_serializer_class(self):
        if self.action in ["create", "update", "partial_update"]:
            return create_day_serializer(
                itinerary_id=self.request.GET.get("itinerary_id", None),
                user=self.request.user,
            )
        else:
            return DaySerializer


class DayMethodView(APIView):
    permission_classes = [IsAuthenticated]

    # TODO Make this method authorisation safe
    def post(self, request, itinerary_id, day_id, method):
        day = get_object_or_404(Day, id=day_id, itinerary__id=itinerary_id)

        if method == "up":
            day.up()
        elif method == "down":
            day.down()
        else:
            return Response(
                {"detail": "Invalid method parameter"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(status=status.HTTP_204_NO_CONTENT)
