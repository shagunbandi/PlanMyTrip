from common.enums import RESERVATION_STATUS
from common.models import OwnerModel, TimestampModel
from django.db import models
from enumchoicefield import EnumChoiceField
from itinerary.models.agenda import Agenda
from ordered_model.models import OrderedModel


class Place(OwnerModel, OrderedModel, TimestampModel):
    title = models.CharField(max_length=120, blank=True, null=True)
    text = models.TextField(blank=True, null=True, default="")
    link = models.CharField(max_length=120, null=True, blank=True)
    file = models.FileField(upload_to="reservations/", null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = EnumChoiceField(RESERVATION_STATUS, default=RESERVATION_STATUS.UNSET)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    currency = models.CharField(max_length=3, null=True, blank=True, default="EUR")
    agenda = models.ForeignKey(
        Agenda,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="agendas",
    )

    order_with_respect_to = "agenda__itinerary"

    def save(self, *args, **kwargs):
        if self.file.name:
            filename = f"{self.id}_{self.file.name}"
            self.file.name = (
                f"{self.user.id}/{self.content_type.model}/place/{filename}"
            )

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
