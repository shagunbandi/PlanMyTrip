from common.enums import RESERVATION_STATUS
from common.mixins import AuthBasicInfoMixin, OrderMixin, TimestampsMixin
from day.models import Day
from django.core.validators import MinValueValidator
from django.db import models
from enumchoicefield import EnumChoiceField


class Place(TimestampsMixin, AuthBasicInfoMixin, OrderMixin):
    place_id = models.CharField(max_length=120, null=True, blank=True)
    reservation_link = models.CharField(max_length=120, null=True, blank=True)
    reservation_file = models.FileField(
        upload_to="reservations/", null=True, blank=True
    )
    reservation_date = models.DateField(null=True, blank=True)
    reservation_time = models.TimeField(null=True, blank=True)
    reservation_status = EnumChoiceField(
        RESERVATION_STATUS, default=RESERVATION_STATUS.NO
    )
    reservation_cost = models.FloatField(
        null=True, blank=True, validators=[MinValueValidator(0)]
    )
    currency = models.CharField(max_length=3, null=True, blank=True)

    day = models.ForeignKey(
        Day, on_delete=models.CASCADE, related_name="places", null=False
    )
    order_with_respect_to = "day"

    def save(self, *args, **kwargs):
        if self.reservation_file.name:
            filename = f"{self.id}_{self.reservation_file.name}"
            self.reservation_file.name = f"{self.user.id}/itinerary/place/{filename}"

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ("order",)
