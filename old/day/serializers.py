from common.serializers import (
    CreateMixinSerializer,
    OrderMixinSerializer,
    ValidateParentMixinSerializer,
)
from itinerary.models import Itinerary
from ordered_model.models import OrderedModel
from place.serializers import PlaceSerializer
from rest_framework.serializers import IntegerField

from .models import Day


class DaySerializer(OrderMixinSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta(OrderedModel.Meta):
        model = Day
        fields = "__all__"


def create_day_serializer(itinerary_id=None, user=None):
    class CreateDaySerializer(
        ValidateParentMixinSerializer,
        CreateMixinSerializer,
    ):
        class Meta:
            model = Day
            exclude = ["itinerary"]

        def validate(self, data):
            return super().validate_parent(
                Itinerary, "itinerary_id", itinerary_id, user, data
            )

        def create(self, validated_data):
            return super().create(validated_data)

    return CreateDaySerializer