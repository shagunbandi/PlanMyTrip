from rest_framework import serializers


class CreateMixinSerializer(serializers.ModelSerializer):
    def create(self, validated_data):
        user = self.context["request"].user
        validated_data["user"] = user
        model = self.Meta.model
        return model.objects.create(**validated_data)
