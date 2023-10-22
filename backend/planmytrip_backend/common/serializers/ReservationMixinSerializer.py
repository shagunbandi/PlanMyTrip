from rest_framework import serializers
from common.mixins import ReservationMixin
from common.enums import RESERVATION_STATUS
from rest_enumfield import EnumField


class ReservationMixinSerializer(serializers.Serializer):
    reservation_place_id = serializers.CharField(
        max_length=120, allow_null=True, allow_blank=True
    )
    reservation_link = serializers.CharField(
        max_length=120, allow_null=True, allow_blank=True
    )
    reservation_date = serializers.DateField(allow_null=True)
    reservation_time = serializers.TimeField(allow_null=True)
    reservation_status = EnumField(
        choices=RESERVATION_STATUS,
        to_choice=lambda x: x.value,
        default=RESERVATION_STATUS.NO,
    )

    reservation_file = serializers.FileField(
        allow_null=True, allow_empty_file=True, use_url=False
    )

    class Meta:
        fields = (
            "reservation_place_id",
            "reservation_link",
            "reservation_date",
            "reservation_time",
            "reservation_status",
            "reservation_file",
        )
