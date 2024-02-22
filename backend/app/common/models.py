from django.contrib.auth.models import User
from django.db import models
from django.db.models import F
from django.utils import timezone


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        abstract = True


class GenericRelationOrderModel(models.Model):
    order = models.PositiveIntegerField(default=0)

    def _move(self, obj, up=True):
        queryset = self.__class__.objects.filter(
            content_type=obj.content_type, object_id=obj.object_id
        )
        if up:
            queryset = queryset.filter(order__lt=obj.order).order_by("-order")
        else:
            queryset = queryset.filter(order__gt=obj.order).order_by("order")

        try:
            target_obj = queryset[0]
            obj.order, target_obj.order = target_obj.order, obj.order
            obj.save(update_fields=["order"])
            target_obj.save(update_fields=["order"])
        except IndexError:
            pass

    def up(self):
        self._move(self, up=True)

    def down(self):
        self._move(self, up=False)

    def insert(self, obj, before=None, after=None):
        if before:
            queryset = self.__class__.objects.filter(
                content_type=obj.content_type,
                object_id=obj.object_id,
                order__lt=before.order,
            )
            queryset.update(order=F("order") + 1)
            obj.order = before.order - 1
        elif after:
            queryset = self.__class__.objects.filter(
                content_type=obj.content_type,
                object_id=obj.object_id,
                order__gt=after.order,
            )
            queryset.update(order=F("order") + 1)
            obj.order = after.order + 1
        else:
            obj.order = (
                self.__class__.objects.filter(
                    content_type=obj.content_type, object_id=obj.object_id
                ).count()
                + 1
            )
        obj.save()

        return obj

    def save(self, *args, **kwargs):
        if not self.order:
            # Get the maximum order value and increment it by 1
            max_order = self.__class__.objects.filter(
                content_type=self.content_type, object_id=self.object_id
            ).aggregate(max_order=models.Max("order"))["max_order"]
            self.order = max_order + 1 if max_order is not None else 1
        super().save(*args, **kwargs)

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
