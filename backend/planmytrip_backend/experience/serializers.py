from rest_framework import serializers
from .models import Experience, GoogleMapsPlaces


class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = "__all__"


# class GoogleMapsPlacesSerialiser(serializers.Serializer):
#     placed_id = serializers.CharField()
#     city = serializers.CharField(max_length=200)
#     rating_value = serializers.IntegerField()
#     rating_count = serializers.IntegerField()
#     latitude = serializers.FloatField()
#     longitude = serializers.FloatField()
