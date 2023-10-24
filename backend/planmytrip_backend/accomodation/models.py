from django.db import models
from common.mixins import TimestampsMixin, AuthBasicInfoMixin
from day.models import Day
from ordered_model.models import OrderedModel


class Accomodation(TimestampsMixin, AuthBasicInfoMixin, OrderedModel):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="accomodations", null=False
    )

    order_with_respect_to = "day"

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
