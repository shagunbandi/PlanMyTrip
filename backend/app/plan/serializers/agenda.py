from common.serializers import CreateSerializer
from plan.models.agenda import Agenda
from plan.serializers.place import PlaceSerializer
from rest_framework import serializers


class AgendaSerializer(CreateSerializer):
    places = PlaceSerializer(many=True, read_only=True)
    order = serializers.IntegerField(read_only=True)

    class Meta:
        model = Agenda
        fields = ["id", "title", "places", "is_itinerary", "order"]
