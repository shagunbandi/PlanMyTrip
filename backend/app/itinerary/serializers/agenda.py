from common.serializers import CreateSerializer, OrderSerializer
from itinerary.models.agenda import Agenda
from itinerary.serializers.place import PlaceSerializer


class AgendaSerializer(OrderSerializer, CreateSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Agenda
        fields = ["id", "title", "places", "order"]
