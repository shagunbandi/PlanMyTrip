from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class GenericRelationMixinSerializer(serializers.ModelSerializer):
    parent_type = serializers.PrimaryKeyRelatedField(queryset=ContentType.objects.all())
    parent_id = serializers.IntegerField()
