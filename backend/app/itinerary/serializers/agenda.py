from common.serializers import CreateSerializer
from itinerary.models.agenda import Agenda
from itinerary.serializers.place import PlaceSerializer
from ordered_model.serializers import OrderedModelSerializer


class AgendaSerializer(OrderedModelSerializer, CreateSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Agenda
        fields = ["id", "title", "places", "order"]
