from common.enums import CHECKED_STATUS
from django.db import models
from enumchoicefield import EnumChoiceField


class CheckboxMixin(models.Model):
    checked_status = EnumChoiceField(CHECKED_STATUS, default=CHECKED_STATUS.UNSELECTED)

    class Meta:
        abstract = True
