from django.contrib.auth.models import User
from django.db import models


class OwnerModel(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=True)

    class Meta:
        abstract = True


from django.db import models
from django.db.models import F


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

    def move_up(self, obj):
        self._move(obj, up=True)

    def move_down(self, obj):
        self._move(obj, up=False)

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

    class Meta:
        abstract = True
