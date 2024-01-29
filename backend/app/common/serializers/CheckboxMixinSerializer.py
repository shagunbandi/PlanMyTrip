from common.enums import CHECKED_STATUS
from rest_enumfield import EnumField
from rest_framework import serializers


class CheckboxMixinSerializer(serializers.Serializer):
    checked_status = EnumField(
        choices=CHECKED_STATUS,
        to_choice=lambda x: x.value,
        default=CHECKED_STATUS.UNSELECTED,
    )
