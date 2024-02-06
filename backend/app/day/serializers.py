from attraction.serializers import AttractionSerializer
from common.serializers import (
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    OrderMixinSerializer,
    TimestampsMixinSerializer,
    ValidateParentMixinSerializer,
)
from itinerary.models import Itinerary
from ordered_model.models import OrderedModel
from rest_framework.serializers import IntegerField

from .models import Day


class DaySerializer(
    AuthBasicInfoMixinSerializer, TimestampsMixinSerializer, OrderMixinSerializer
):
    attractions = AttractionSerializer(many=True, read_only=True)

    class Meta(OrderedModel.Meta):
        model = Day
        fields = "__all__"


def create_day_serializer(itinerary_id=None, user=None):
    class CreateDaySerializer(
        AuthBasicInfoMixinSerializer,
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
