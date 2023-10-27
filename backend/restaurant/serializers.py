from rest_framework.serializers import IntegerField
from .models import Restaurant
from day.models import Day
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    OrderMixinSerializer,
    ValidateParentMixinSerializer,
    ReservationMixinSerializer,
)


class RestaurantSerializer(
    AuthBasicInfoMixinSerializer,
    OrderMixinSerializer,
    TimestampsMixinSerializer,
    ReservationMixinSerializer,
):
    id = IntegerField(read_only=True)
    order = IntegerField(read_only=True)

    class Meta:
        model = Restaurant
        fields = "__all__"


def create_restaurant_serializer(day_id=None, user=None):
    class CreateRestaurantSerializer(
        AuthBasicInfoMixinSerializer,
        ValidateParentMixinSerializer,
        OrderMixinSerializer,
        CreateMixinSerializer,
        ReservationMixinSerializer,
    ):
        class Meta:
            model = Restaurant
            exclude = ["day"]

        def validate(self, data):
            return self.validate_parent(Day, "day_id", day_id, user, data)

        def create(self, validated_data):
            return super().create(validated_data)

    return CreateRestaurantSerializer
