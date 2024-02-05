from common.enums import RESERVATION_STATUS
from django.core.validators import MinValueValidator
from django.db import models
from enumchoicefield import EnumChoiceField


class ReservationMixin(models.Model):
    reservation_place_id = models.CharField(max_length=120, null=True, blank=True)
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

    def save(self, *args, **kwargs):
        if self.reservation_file.name:
            filename = f"{self.id}_{self.reservation_file.name}"
            self.reservation_file.name = f"itinerary/itinerary_{self.day.itinerary.id}/day_{self.day.id}/{self.__class__.__name__}/{filename}"

        super().save(*args, **kwargs)

    class Meta:
        abstract = True
