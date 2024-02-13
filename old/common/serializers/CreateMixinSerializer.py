from rest_framework import serializers


class CreateMixinSerializer(serializers.ModelSerializer):
    """
    A mixin for creating objects with the authenticated user as the owner.

    This mixin provides a custom implementation of the create() method,
    which automatically sets the authenticated user as the owner of the object being created.
    """

    def create(self, validated_data):
        """
        Create a new object instance with the authenticated user as the owner.

        Args:
            validated_data (dict): The validated data to create the object.

        Returns:
            obj: The newly created object.
        """
        # Get the authenticated user from the request context
        user = self.context["request"].user

        # Set the authenticated user as the owner of the object
        validated_data["user"] = user

        # Get the model class from the serializer's Meta class
        model = self.Meta.model

        # Create a new object instance with the provided validated data
        return model.objects.create(**validated_data)
