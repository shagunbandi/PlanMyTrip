from rest_framework.serializers import ValidationError
from .models import Dish
from day.models import Day
from common.serializers import (
    TimestampsMixinSerializer,
    AuthBasicInfoMixinSerializer,
    CreateMixinSerializer,
    SequenceMixinSerializer,
)


class DishSerializer(
    AuthBasicInfoMixinSerializer, SequenceMixinSerializer, TimestampsMixinSerializer
):
    class Meta:
        model = Dish
        fields = "__all__"


def create_dish_serializer(day_id=None, user=None):
    class CreateDishSerializer(
        AuthBasicInfoMixinSerializer, CreateMixinSerializer, SequenceMixinSerializer
    ):
        class Meta:
            model = Dish
            exclude = ["day"]

        def __init__(self, *args, **kwargs):
            self.day_instance = None
            if day_id:
                day_qs = Day.objects.filter(id=day_id, user=user)
                if day_qs.exists() and day_qs.count() == 1:
                    self.day_instance = day_qs.first()
            return super(CreateDishSerializer, self).__init__(*args, **kwargs)

        def validate(self, data):
            if not day_id or not self.day_instance:
                raise ValidationError("Day Id is not valid")
            data["day"] = self.day_instance
            return data

        def create(self, validated_data):
            return super().create(validated_data, Day)

    return CreateDishSerializer
