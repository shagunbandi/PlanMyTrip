from common.mixins import AuthBasicInfoMixin, CheckboxMixin, TimestampsMixin
from day.models import Day
from django.db import models
from ordered_model.models import OrderedModel


class Dish(TimestampsMixin, AuthBasicInfoMixin, OrderedModel, CheckboxMixin):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="dishes", null=False
    )

    order_with_respect_to = "day"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
