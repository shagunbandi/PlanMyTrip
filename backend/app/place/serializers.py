from common.enums import RESERVATION_STATUS
from common.serializers import CreateMixinSerializer, OrderMixinSerializer

from .models import Place


class PlaceSerializer(
    OrderMixinSerializer,
    CreateMixinSerializer,
):
    class Meta:
        model = Place
        fields = "__all__"
