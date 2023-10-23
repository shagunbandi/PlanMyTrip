from django.db import models


class ItineraryElement(models.Model):
    """
    Itinerary element
    """

    compound = models.ForeignKey("planner.ItineraryCompound", on_delete=models.CASCADE)
    place_id = models.CharField(max_length=64)
    name = models.CharField(max_length=64)
    city = models.CharField(max_length=64, null=True)
    category = models.CharField(max_length=64, null=True)
    activity_time_in_mins = models.IntegerField(default=-1)
    rating_value = models.FloatField(null=True)
    rating_count = models.IntegerField(null=True)
    duration_in_mins = models.FloatField(null=True)
    distance_in_meters = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    nth_day = models.IntegerField(null=True)
    activity_number = models.IntegerField(null=True)
