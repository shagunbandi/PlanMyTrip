from rest_framework.serializers import ValidationError, IntegerField
from .models import Day
from itinerary.models import Itinerary
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    SequenceMixinSerializer,
    ValidateParentMixinSerializer,
)
from dish.serializers import DishSerializer


class DaySerializer(
    AuthBasicInfoMixinSerializer,
    SequenceMixinSerializer,
    TimestampsMixinSerializer,
):
    dishes = DishSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = "__all__"


def create_day_serializer(itinerary_id=None, user=None):
    class CreateDaySerializer(
        AuthBasicInfoMixinSerializer,
        CreateMixinSerializer,
        SequenceMixinSerializer,
        ValidateParentMixinSerializer,
    ):
        class Meta:
            model = Day
            exclude = ["itinerary"]

        # def __init__(self, *args, **kwargs):
        #     self.itinerary_instance = None
        #     if itinerary_id:
        #         itinerary_qs = Itinerary.objects.filter(id=itinerary_id, user=user)
        #         if itinerary_qs.exists() and itinerary_qs.count() == 1:
        #             self.itinerary_instance = itinerary_qs.first()
        #     return super(CreateDaySerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            return super().validate_parent(
                Itinerary, "itinerary_id", itinerary_id, user, data
            )
            # return super().validate(itinerary_id, self.itinerary_instance, data)

        def create(self, validated_data):
            return super().create(validated_data, Day)

    return CreateDaySerializer
