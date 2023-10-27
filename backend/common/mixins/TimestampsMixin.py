from django.db import models


class TimestampsMixin(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    class Meta:
        abstract = True
