from common.serializers import CreateSerializer, GenericRelationSerializer

from .models import Day, Itinerary, Places


class PlaceSerializer(GenericRelationSerializer, CreateSerializer):
    class Meta:
        model = Places
        fields = ["title", "id", "content_type", "object_id"]


class DaySerializer(CreateSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ["title", "id", "places"]


class ItinerarySerializer(CreateSerializer):
    days = DaySerializer(many=True, read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ["title", "id", "days", "places"]
