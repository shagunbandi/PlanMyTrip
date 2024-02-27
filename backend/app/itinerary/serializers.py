from common.serializers import (
    CreateSerializer,
    GenericRelationSerializer,
    OrderSerializer,
)

from .models import Day, Itinerary, Place


class PlaceSerializer(GenericRelationSerializer, OrderSerializer, CreateSerializer):
    class Meta:
        model = Place
        fields = [
            "id",
            "title",
            "text",
            "order",
            "content_type",
            "object_id",
            "link",
            "file",
            "date",
            "time",
            "status",
            "cost",
            "currency",
        ]


class DaySerializer(OrderSerializer, CreateSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ["id", "title", "order", "places"]


class ItinerarySerializer(CreateSerializer):
    days = DaySerializer(many=True, read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ["id", "title", "days", "places", "created_at", "updated_at"]
