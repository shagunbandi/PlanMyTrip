from common.serializers import (
    AuthBasicInfoMixinSerializer,
    CheckboxMixinSerializer,
    CreateMixinSerializer,
    OrderMixinSerializer,
    TimestampsMixinSerializer,
    ValidateParentMixinSerializer,
)
from day.models import Day
from rest_framework.serializers import IntegerField

from .models import Dish


class DishSerializer(
    AuthBasicInfoMixinSerializer,
    OrderMixinSerializer,
    TimestampsMixinSerializer,
    CheckboxMixinSerializer,
):
    id = IntegerField(read_only=True)
    order = IntegerField(read_only=True)

    class Meta:
        model = Dish
        fields = "__all__"


def create_dish_serializer(day_id=None, user=None):
    class CreateDishSerializer(
        AuthBasicInfoMixinSerializer,
        ValidateParentMixinSerializer,
        OrderMixinSerializer,
        CreateMixinSerializer,
        CheckboxMixinSerializer,
    ):
        class Meta:
            model = Dish
            exclude = ["day"]

        def validate(self, data):
            return self.validate_parent(Day, "day_id", day_id, user, data)

        def create(self, validated_data):
            return super().create(validated_data)

    return CreateDishSerializer
