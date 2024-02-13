from common.mixins import CreateMixin
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers

from .models import Day, Itinerary, Places


class PlaceSerializer(CreateMixin, serializers.ModelSerializer):
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

    class Meta:
        model = Places
        fields = ["title", "id", "content_type", "object_id"]


class DaySerializer(CreateMixin, serializers.ModelSerializer):
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Day
        fields = ["title", "id", "places"]


class ItinerarySerializer(CreateMixin, serializers.ModelSerializer):
    days = DaySerializer(many=True, read_only=True)
    places = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ["title", "id", "days", "places"]
