from common.serializers import CreateSerializer, OrderSerializer
from itinerary.models.itinerary import Itinerary
from itinerary.serializers.place import PlaceSerializer
from itinerary.serializers.roster import RosterSerializer


class ItinerarySerializer(CreateSerializer):
    rosters = RosterSerializer(many=True, read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ["id", "title", "rosters", "created_at", "updated_at"]
