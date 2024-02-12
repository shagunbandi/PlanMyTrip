from django.contrib.contenttypes.models import ContentType
from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ValidationError


class ValidateParentMixinSerializer(serializers.Serializer):
    """
    A mixin for validating the existence of a parent object.

    This mixin provides a method to validate the existence of a parent object
    based on the provided parent ID and user, and update the data dictionary
    with the ID of the parent object if it exists.
    """

    def validate_parent(self, model, parent_key_name, parent_id, user, data):
        """
        Validate the existence of a parent object and update the data dictionary.

        Args:
            model (Model): The parent model class.
            parent_key_name (str): The name of the key in the data dictionary
                corresponding to the parent object ID.
            parent_id (int): The ID of the parent object to validate.
            user (User): The authenticated user.
            data (dict): The data dictionary to update with the parent object ID.

        Returns:
            dict: The updated data dictionary with the parent object ID.

        Raises:
            ValidationError: If the parent object does not exist or is not valid.
        """
        parent_instance = None

        # Query the parent model to check if the parent object exists and belongs to the user
        parent_qs = model.objects.filter(id=parent_id, user=user)

        # If a single matching parent object is found, assign it to parent_instance
        if parent_qs.exists() and parent_qs.count() == 1:
            parent_instance = parent_qs.first()

        # If no valid parent instance is found, raise a ValidationError
        if not parent_instance:
            raise ValidationError(f"{model.__name__} is not valid")

        # Update the data dictionary with the ID of the parent instance
        data[parent_key_name] = parent_instance.id

        return data


class ValidateParentTypeMixinSerializer(serializers.ModelSerializer):
    def validate(self, attrs):
        breakpoint()
        parent_type_name = attrs["parent_type_name"]
        parent_id = attrs["parent_id"]

        # Get the content type dynamically based on parent_type_name
        parent_content_type = ContentType.objects.filter(model=parent_type_name).first()

        if not parent_content_type:
            raise serializers.ValidationError("Invalid parent type")

        # Check if the parent object exists
        parent_obj = (
            parent_content_type.model_class().objects.filter(pk=parent_id).exists()
        )
        if not parent_obj:
            raise serializers.ValidationError("Parent object does not exist")

        return attrs
