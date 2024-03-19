from common.exceptions import ValidationException
from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404
from itinerary.models.agenda import Agenda
from itinerary.models.itinerary import Itinerary
from itinerary.serializers.agenda import AgendaSerializer
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView


class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer
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
        itinerary = Itinerary.objects.filter(owner=self.request.user, id=itinerary_id)
        if itinerary.exists():
            serializer.save(itinerary_id=itinerary_id)
        else:
            raise ValueError("Itinerary does not exist")


class MoveAgendaView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, itinerary_id, agenda_id):
        method = request.data.get("method", "")
        agenda = get_object_or_404(
            Agenda, owner=request.user, id=agenda_id, itinerary__id=itinerary_id
        )
        if method == "up":
            agenda.up()
        elif method == "down":
            agenda.down()
        else:
            raise ValidationException("Invalid method parameter")
        return Response(status=status.HTTP_204_NO_CONTENT)
