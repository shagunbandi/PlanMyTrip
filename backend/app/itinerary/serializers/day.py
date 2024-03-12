from common.serializers import CreateSerializer, OrderSerializer
from itinerary.models.day import Day
from itinerary.serializers.place import PlaceSerializer


class DaySerializer(OrderSerializer, CreateSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ["id", "title", "places", "order"]
