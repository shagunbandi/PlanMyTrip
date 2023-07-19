from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.MapsOverview, name=''),
    path('distance', views.distance_with_place_ids, name='distance'),
]
