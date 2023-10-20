from rest_framework import serializers
from .models import Itinerary
from rest_framework import serializers


class ItinerarySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, allow_blank=False, trim_whitespace=True)
    description = serializers.CharField(
        max_length=180, allow_blank=True, trim_whitespace=True
    )
    timeline = serializers.ListField()

    class Meta:
        model = Itinerary
        fields = "__all__"
