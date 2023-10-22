class CreateMixinSerializer:
    def create(self, validated_data, model_class):
        user = self.context["request"].user
        validated_data["user"] = user

        return model_class.objects.create(**validated_data)
