from django.db import models


class OrderMixin(models.Model):
    order = models.IntegerField(blank=True, default=-1)

    class Meta:
        abstract = True
