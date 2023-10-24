from rest_framework.serializers import IntegerField
from .models import Day
from itinerary.models import Itinerary
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    ValidateParentMixinSerializer,
)
from ordered_model.models import OrderedModel
from dish.serializers import DishSerializer
from accomodation.serializers import AccomodationSerializer
from restaurant.serializers import RestaurantSerializer


class DaySerializer(
    AuthBasicInfoMixinSerializer,
    TimestampsMixinSerializer,
):
    dishes = DishSerializer(many=True, read_only=True)
    accomodations = AccomodationSerializer(many=True, read_only=True)
    restaurants = RestaurantSerializer(many=True, read_only=True)
    id = IntegerField(read_only=True)
    order = IntegerField(read_only=True)

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
