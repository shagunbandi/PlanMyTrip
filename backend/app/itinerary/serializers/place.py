from common.serializers import CreateSerializer, OrderSerializer
from itinerary.models.place import Place


class PlaceSerializer(OrderSerializer, CreateSerializer):
    class Meta:
        model = Place
        fields = [
            "id",
            "title",
            "text",
            "link",
            "file",
            "date",
            "time",
            "status",
            "cost",
            "currency",
            "order",
        ]
