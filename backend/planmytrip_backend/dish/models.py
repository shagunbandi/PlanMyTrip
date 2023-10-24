from django.db import models
from common.mixins import TimestampsMixin, AuthBasicInfoMixin, OrderMixin
from day.models import Day


class Dish(TimestampsMixin, AuthBasicInfoMixin, OrderMixin):
    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="dishes", null=False
    )

    def __str__(self):
        return self.name
