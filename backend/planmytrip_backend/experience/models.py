from django.db import models
from django.contrib.auth.models import User
from enumchoicefield import ChoiceEnum, EnumChoiceField


class ExperienceTypes(ChoiceEnum):
    EATERY = "eatery"
    EXPERIENCE = "experience"
    MONUMENT = "monument"
    OTHER = "other"


class Experience(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=180)
    type = EnumChoiceField(ExperienceTypes, default=ExperienceTypes.EXPERIENCE)
    google_place_id = models.CharField(max_length=120, null=True)
    # ticket = models.

    # User Info
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    # Metadata
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated = models.DateTimeField(auto_now=True, blank=True)

    # @property
    # def google_maps_data(self):
    #     google_place = {}
    #     # google_place['place_id'] =

    def __str__(self):
        return self.name


# # Not a DB table
# class GoogleMapsPlaces:
#     def __init__(
#         self, places_id, city, rating_value, rating_count, latitude, longitude
#     ):
#         self.places_id = places_id
#         self.city = city
#         self.rating_value = rating_value
#         self.rating_count = rating_count
#         self.latitude = latitude
#         self.longitude = longitude
