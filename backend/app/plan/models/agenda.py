from common.models import OwnerModel, TimestampModel
from django.db import models
from ordered_model.models import OrderedModel
from plan.models.plan import Plan


class Agenda(OwnerModel, OrderedModel, TimestampModel):
    title = models.CharField(max_length=120, null=True, blank=True)
    plan = models.ForeignKey(
        Plan,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        related_name="agendas",
    )

    order_with_respect_to = "plan"

    def __str__(self):
        return self.title

    class Meta:
        ordering = ("order",)
