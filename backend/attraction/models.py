from common.enums import Category
from common.mixins import (
    AuthBasicInfoMixin,
    CheckboxMixin,
    ReservationMixin,
    TimestampsMixin,
)
from day.models import Day
from django.db import models
from enumchoicefield import EnumChoiceField
from ordered_model.models import OrderedModel


class Attraction(
    TimestampsMixin, AuthBasicInfoMixin, ReservationMixin, OrderedModel, CheckboxMixin
):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="attractions", null=False
    )
    category = EnumChoiceField(Category, default=Category.EXPERIENCE)
    order_with_respect_to = "day"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
