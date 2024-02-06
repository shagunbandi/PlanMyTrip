from common.enums import RESERVATION_STATUS
from common.serializers import (
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    OrderMixinSerializer,
    TimestampsMixinSerializer,
    ValidateParentMixinSerializer,
)
from day.models import Day
from django.core.validators import MinValueValidator
from rest_enumfield import EnumField
from rest_framework import serializers

from .models import Attraction


class BaseAttractionSerializer(
    AuthBasicInfoMixinSerializer, TimestampsMixinSerializer, OrderMixinSerializer
):
    place_id = serializers.CharField(
        max_length=120, allow_null=True, allow_blank=True, required=False
    )
    reservation_link = serializers.CharField(
        max_length=120, allow_null=True, allow_blank=True, required=False
    )
    reservation_date = serializers.DateField(allow_null=True, required=False)
    reservation_time = serializers.TimeField(allow_null=True, required=False)
    reservation_status = EnumField(
        choices=RESERVATION_STATUS,
        to_choice=lambda x: x.value,
        default=RESERVATION_STATUS.NO,
        required=False,
    )
    reservation_file = serializers.FileField(
        allow_null=True, allow_empty_file=True, use_url=False, required=False
    )
    reservation_cost = serializers.FloatField(
        allow_null=True, required=False, validators=[MinValueValidator(0)]
    )
    currency = serializers.CharField(
        max_length=3, allow_blank=True, allow_null=True, default="EUR"
    )


class AttractionSerializer(BaseAttractionSerializer):
    class Meta:
        model = Attraction
        fields = "__all__"


def create_attraction_serializer(day_id=None, user=None):
    class CreateAttractionSerializer(
        BaseAttractionSerializer, ValidateParentMixinSerializer, CreateMixinSerializer
    ):
        class Meta:
            model = Attraction
            exclude = ["day"]

        def validate(self, data):
            return self.validate_parent(Day, "day_id", day_id, user, data)

        def create(self, validated_data):
            return super().create(validated_data)

    return CreateAttractionSerializer
