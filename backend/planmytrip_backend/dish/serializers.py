from rest_framework.serializers import ValidationError
from .models import Dish
from day.models import Day
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    SequenceMixinSerializer,
    ValidateParentMixinSerializer,
)


class DishSerializer(
    AuthBasicInfoMixinSerializer, SequenceMixinSerializer, TimestampsMixinSerializer
):
    class Meta:
        model = Dish
        fields = "__all__"


def create_dish_serializer(day_id=None, user=None):
    class CreateDishSerializer(
        AuthBasicInfoMixinSerializer,
        CreateMixinSerializer,
        SequenceMixinSerializer,
        ValidateParentMixinSerializer,
    ):
        class Meta:
            model = Dish
            exclude = ["day"]

        def validate(self, data):
            return super().validate_parent(Day, "day_id", day_id, user, data)

        def create(self, validated_data):
            return super().create(validated_data, Day)

    return CreateDishSerializer
