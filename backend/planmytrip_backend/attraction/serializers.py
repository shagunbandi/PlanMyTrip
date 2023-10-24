from rest_framework.serializers import IntegerField
from .models import Attraction, Category
from day.models import Day
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    SequenceMixinSerializer,
    ValidateParentMixinSerializer,
)
from rest_enumfield import EnumField


class AttractionSerializer(
    AuthBasicInfoMixinSerializer, SequenceMixinSerializer, TimestampsMixinSerializer
):
    id = IntegerField(read_only=True)
    category = EnumField(choices=Category, to_choice=lambda x: x.value)

    class Meta:
        model = Attraction
        fields = "__all__"


def create_attraction_serializer(day_id=None, user=None):
    class CreateAttractionSerializer(
        AuthBasicInfoMixinSerializer,
        CreateMixinSerializer,
        SequenceMixinSerializer,
        ValidateParentMixinSerializer,
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
