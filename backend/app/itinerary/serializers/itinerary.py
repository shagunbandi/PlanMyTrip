from common.serializers import CreateSerializer, OrderSerializer
from itinerary.models.itinerary import Itinerary
from itinerary.serializers.agenda import AgendaSerializer
from itinerary.serializers.place import PlaceSerializer


class ItinerarySerializer(CreateSerializer):
    agendas = AgendaSerializer(many=True, read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ["id", "title", "agendas", "created_at", "updated_at"]
