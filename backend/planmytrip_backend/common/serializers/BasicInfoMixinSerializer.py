from rest_framework import serializers
from django.contrib.auth.models import User  # Import User model if not already imported


class BasicInfoMixinSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=60)
    notes = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        fields = ("name", "notes")


class AuthBasicInfoMixinSerializer(BasicInfoMixinSerializer):
    user = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(), required=False, write_only=True
    )

    class Meta:
        fields = ("name", "notes", "user")
