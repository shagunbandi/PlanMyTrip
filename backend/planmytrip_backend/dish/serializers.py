from rest_framework.serializers import IntegerField
from .models import Dish
from day.models import Day
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    OrderMixinSerializer,
    ValidateParentMixinSerializer,
)


class DishSerializer(
    AuthBasicInfoMixinSerializer, OrderMixinSerializer, TimestampsMixinSerializer
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
    ):
        class Meta:
            model = Dish
            exclude = ["day"]

        def validate(self, data):
            return self.validate_parent(Day, "day_id", day_id, user, data)

        def create(self, validated_data):
            return super().create(validated_data)

    return CreateDishSerializer
