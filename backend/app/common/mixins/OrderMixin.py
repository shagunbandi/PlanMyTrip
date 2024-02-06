from django.db import models
from ordered_model.models import OrderedModel


class OrderMixin(OrderedModel):
    """
    A mixin for models to add ordering functionality.

    This mixin provides a field to specify the order of instances when querying or displaying them.

    Attributes:
        order (int): The order of the instance.

    Note:
        By default, the order is set to -1, indicating that it hasn't been explicitly ordered.
    """

    order = models.IntegerField(blank=True, default=-1)

    class Meta:
        abstract = True
