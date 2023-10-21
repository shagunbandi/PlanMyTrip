from rest_framework import serializers
from .models import Itinerary
from experience.models import Experience
from experience.serializers import ExperienceSerializer
from rest_framework import serializers


class ItinerarySerializer(serializers.ModelSerializer):
    name = serializers.CharField(max_length=60, allow_blank=False, trim_whitespace=True)
    description = serializers.CharField(
        max_length=180, allow_blank=False, trim_whitespace=True
    )
    timeline = serializers.ListField()

    def validate_timeline(self, timeline):
        # Validate timeline format
        if not isinstance(timeline, list):
            raise serializers.ValidationError("Timeline must be a list.")
        # Validate the count of such fields in db is same as the number of ids provided
        if not Experience.objects.filter(
            id__in=timeline, user=self.initial_data["user"]
        ).count() == len(timeline):
            raise serializers.ValidationError("Experiences in timeline must exist")
        return timeline

    class Meta:
        model = Itinerary
        fields = "__all__"


class ItineraryWithExperiencesSerializer(ItinerarySerializer):
    # detailed_timeline = ExperienceSerializer(many=True)

    class Meta:
        model = Itinerary
        fields = ["name", "description", "timeline"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        experiences = Experience.objects.filter(
            id__in=instance.timeline, user=instance.user
        )

        # Replace the list of IDs with the serialized author data
        data["timeline"] = ExperienceSerializer(experiences, many=True).data

        return data
