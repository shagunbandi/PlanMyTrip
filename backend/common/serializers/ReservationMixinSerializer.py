from common.enums import RESERVATION_STATUS
from common.mixins import ReservationMixin
from rest_enumfield import EnumField
from rest_framework import serializers


class ReservationMixinSerializer(serializers.Serializer):
    reservation_place_id = serializers.CharField(
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
