from common.serializers import CreateSerializer
from itinerary.models.itinerary import Itinerary
from itinerary.serializers.agenda import AgendaSerializer
from itinerary.serializers.place import PlaceSerializer


class ItinerarySerializer(CreateSerializer):
    agendas = AgendaSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = [
            "id",
            "title",
            "agendas",
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]
