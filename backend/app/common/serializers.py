from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class CreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["owner"] = user
        return self.Meta.model.objects.create(**validated_data)


class OrderSerializer(serializers.Serializer):
    order = serializers.IntegerField(read_only=True)
