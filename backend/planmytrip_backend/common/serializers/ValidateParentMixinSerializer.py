from rest_framework import serializers
from django.db import models
from rest_framework.serializers import ValidationError


class ValidateParentMixinSerializer(serializers.Serializer):
    def validate_parent(self, model, parent_key_name, parent_id, user, data):
        parent_instance = None
        day_qs = model.objects.filter(id=parent_id, user=user)
        if day_qs.exists() and day_qs.count() == 1:
            parent_instance = day_qs.first()

        if not parent_instance:
            raise ValidationError(f"{model.__name__} is not valid")
        data[parent_key_name] = parent_instance.id
        return data
