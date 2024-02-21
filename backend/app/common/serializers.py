from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class CreateSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["owner"] = user
        return self.Meta.model.objects.create(**validated_data)


class OrderSerializer(serializers.Serializer):
    order = serializers.IntegerField(read_only=True)


class GenericRelationSerializer(serializers.Serializer):

    content_type = serializers.CharField(required=True)

    def validate_content_type(self, value):
        content_type = ContentType.objects.filter(model=value.lower()).first()
        if not content_type:
            raise serializers.ValidationError("Invalid content type.")

        return content_type

    def validate(self, attrs):
        model = attrs.get("content_type").model_class()
        model_object = model.objects.filter(
            owner=self.context["request"].user, pk=attrs["object_id"]
        ).first()
        if not model_object:
            raise serializers.ValidationError("model does not exist.")
        return super().validate(attrs)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["content_type"] = representation["content_type"].split(" | ")[-1]
        return representation
