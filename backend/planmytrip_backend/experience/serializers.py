from rest_framework import serializers
from .models import Experience, GoogleMapsPlaces


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"
