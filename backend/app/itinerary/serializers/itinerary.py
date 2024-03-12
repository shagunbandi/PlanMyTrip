from common.serializers import CreateSerializer, OrderSerializer
from itinerary.models.itinerary import Itinerary
from itinerary.serializers.day import DaySerializer
from itinerary.serializers.place import PlaceSerializer


class ItinerarySerializer(CreateSerializer):
    days = DaySerializer(many=True, read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ["id", "title", "days", "created_at", "updated_at"]
