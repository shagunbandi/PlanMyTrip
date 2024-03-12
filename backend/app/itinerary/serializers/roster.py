from common.serializers import CreateSerializer, OrderSerializer
from itinerary.models.roster import Roster
from itinerary.serializers.place import PlaceSerializer


class RosterSerializer(OrderSerializer, CreateSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Roster
        fields = ["id", "title", "places", "order"]
