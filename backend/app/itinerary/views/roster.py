from common.exceptions import ValidationException
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from itinerary.models.itinerary import Itinerary
from itinerary.models.roster import Roster
from itinerary.serializers.roster import RosterSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class RosterViewSet(viewsets.ModelViewSet):
    queryset = Roster.objects.all()
    serializer_class = RosterSerializer
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


class MoveRosterView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, itinerary_id):
        method = request.data.get("method", "")
        roster = Roster.objects.filter(owner=request.user, itinerary__id=itinerary_id)
        if method == "up":
            roster.up()
        elif method == "down":
            roster.down()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
