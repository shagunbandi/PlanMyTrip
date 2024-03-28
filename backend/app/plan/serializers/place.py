from common.serializers import CreateSerializer
from plan.models.place import Place
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
            "cost",
            "record_type",
            "start_time",
            "end_time",
            "file",
            "currency",
            "order",
        ]
