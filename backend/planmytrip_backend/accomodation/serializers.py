from rest_framework.serializers import IntegerField
from .models import Accomodation
from day.models import Day
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    SequenceMixinSerializer,
    ValidateParentMixinSerializer,
)


class AccomodationSerializer(
    AuthBasicInfoMixinSerializer, SequenceMixinSerializer, TimestampsMixinSerializer
):
    id = IntegerField(read_only=True)

    class Meta:
        model = Accomodation
        fields = "__all__"


def create_accomodation_serializer(day_id=None, user=None):
    class CreateAccomodationSerializer(
        AuthBasicInfoMixinSerializer,
        CreateMixinSerializer,
        SequenceMixinSerializer,
        ValidateParentMixinSerializer,
    ):
        class Meta:
            model = Accomodation
            exclude = ["day"]

        def validate(self, data):
            return self.validate_parent(Day, "day_id", day_id, user, data)

        def create(self, validated_data):
            return super().create(validated_data)

    return CreateAccomodationSerializer
