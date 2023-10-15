from django.urls import path
from . import views

urlpatterns = [
    path("distance", views.distance_with_place_ids, name="distance"),
]
