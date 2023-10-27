from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from common.mixins import (
    TimestampsMixin,
    AuthBasicInfoMixin,
    ReservationMixin,
)
from day.models import Day
from ordered_model.models import OrderedModel


class Category(ChoiceEnum):
    HIKING = "hiking"
    MONUMENT = "monument"
    CLASSES = "classes"
    LOCALITY = "locality"
    EXPERIENCE = "experience"
    OTHER = "other"

    def __str__(self):
        return self.value


class Attraction(TimestampsMixin, AuthBasicInfoMixin, ReservationMixin, OrderedModel):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="attractions", null=False
    )
    category = EnumChoiceField(Category, default=Category.OTHER)
    order_with_respect_to = "day"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
