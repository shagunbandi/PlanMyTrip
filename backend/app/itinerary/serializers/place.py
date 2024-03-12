from common.serializers import CreateSerializer
from itinerary.models.place import Place
from rest_framework import serializers


class PlaceSerializer(CreateSerializer):
    order = serializers.IntegerField(read_only=True)

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
