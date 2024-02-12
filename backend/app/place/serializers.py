from common.enums import RESERVATION_STATUS
from common.serializers import (
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    OrderMixinSerializer,
    TimestampsMixinSerializer,
    ValidateParentTypeMixinSerializer,
)

from .models import Place


class PlaceSerializer(
    AuthBasicInfoMixinSerializer,
    TimestampsMixinSerializer,
    OrderMixinSerializer,
    ValidateParentTypeMixinSerializer,
    CreateMixinSerializer,
):
    class Meta:
        model = Place
        fields = "__all__"
