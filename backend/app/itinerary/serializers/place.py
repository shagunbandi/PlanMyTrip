from common.serializers import CreateSerializer
from itinerary.models.place import Place
from ordered_model.serializers import OrderedModelSerializer


class PlaceSerializer(OrderedModelSerializer, CreateSerializer):
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
