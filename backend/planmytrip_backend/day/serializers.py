from rest_framework.serializers import IntegerField
from .models import Day
from itinerary.models import Itinerary
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    SequenceMixinSerializer,
    ValidateParentMixinSerializer,
)
from dish.serializers import DishSerializer


class DaySerializer(
    AuthBasicInfoMixinSerializer,
    SequenceMixinSerializer,
    TimestampsMixinSerializer,
):
    dishes = DishSerializer(many=True, read_only=True)
    id = IntegerField(read_only=True)

    class Meta:
        model = Day
        fields = "__all__"


def create_day_serializer(itinerary_id=None, user=None):
    class CreateDaySerializer(
        AuthBasicInfoMixinSerializer,
        CreateMixinSerializer,
        SequenceMixinSerializer,
        ValidateParentMixinSerializer,
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
