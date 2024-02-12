from common.enums import RESERVATION_STATUS
from common.serializers import (
    CreateMixinSerializer,
    OrderMixinSerializer,
    ValidateParentTypeMixinSerializer,
)

from .models import Place


class PlaceSerializer(
    OrderMixinSerializer,
    ValidateParentTypeMixinSerializer,
    CreateMixinSerializer,
):
    class Meta:
        model = Place
        fields = "__all__"
