from rest_framework import serializers
from .models import Itinerary
from experience.serializers import ExperienceSerializer
from rest_framework import serializers


class ItinerarySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, allow_blank=False, trim_whitespace=True)
    description = serializers.CharField(
        max_length=180, allow_blank=False, trim_whitespace=True
    )
    experiences = ExperienceSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = "__all__"


class ItineraryNameSerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, allow_blank=False, trim_whitespace=True)
    id = serializers.IntegerField()

    class Meta:
        model = Itinerary
        fields = ["id", "name"]
