from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from django.utils import timezone


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        abstract = True


class TimestampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super().save(*args, **kwargs)
