from .models import Day
from common.serializers import (
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    SequenceMixinSerializer,
)


class DaySerializer(
    AuthBasicInfoMixinSerializer, CreateMixinSerializer, SequenceMixinSerializer
):
    class Meta:
        model = Day
        fields = "__all__"

    def create(self, validated_data):
        return super().create(validated_data, Day)
