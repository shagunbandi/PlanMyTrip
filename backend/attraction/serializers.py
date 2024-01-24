from common.serializers import (
    AuthBasicInfoMixinSerializer,
    CheckboxMixinSerializer,
    CreateMixinSerializer,
    OrderMixinSerializer,
    ReservationMixinSerializer,
    TimestampsMixinSerializer,
    ValidateParentMixinSerializer,
)
from day.models import Day
from rest_enumfield import EnumField
from rest_framework.serializers import IntegerField

from .models import Attraction, Category


class AttractionSerializer(
    AuthBasicInfoMixinSerializer,
    OrderMixinSerializer,
    TimestampsMixinSerializer,
    ReservationMixinSerializer,
    CheckboxMixinSerializer,
):
    id = IntegerField(read_only=True)
    category = EnumField(choices=Category, to_choice=lambda x: x.value)
    order = IntegerField(read_only=True)

    class Meta:
        model = Attraction
        fields = "__all__"


def create_attraction_serializer(day_id=None, user=None):
    class CreateAttractionSerializer(
        AuthBasicInfoMixinSerializer,
        ValidateParentMixinSerializer,
        OrderMixinSerializer,
        CreateMixinSerializer,
        CheckboxMixinSerializer,
    ):
        category = EnumField(choices=Category, to_choice=lambda x: x.value)

        class Meta:
            model = Attraction
            exclude = ["day"]

        def validate(self, data):
            return self.validate_parent(Day, "day_id", day_id, user, data)

        def create(self, validated_data):
            return super().create(validated_data)

    return CreateAttractionSerializer
