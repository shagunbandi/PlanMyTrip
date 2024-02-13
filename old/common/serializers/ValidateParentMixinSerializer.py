from django.contrib.contenttypes.models import ContentType
from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class ValidateParentMixinSerializer(serializers.Serializer):
    def validate_parent(self, model, parent_key_name, parent_id, user, data):
        parent_instance = None

        parent_qs = model.objects.filter(id=parent_id, user=user)
        if parent_qs.exists() and parent_qs.count() == 1:
            parent_instance = parent_qs.first()
        if not parent_instance:
            raise ValidationError(f"{model.__name__} is not valid")
        data[parent_key_name] = parent_instance.id
        return data
