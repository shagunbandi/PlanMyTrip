from django.db import models
from enumchoicefield import ChoiceEnum, EnumChoiceField
from common.enums import RESERVATION_STATUS


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

    class Meta:
        abstract = True
