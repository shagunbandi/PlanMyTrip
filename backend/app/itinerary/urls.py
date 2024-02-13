from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DayViewSet, ItineraryViewSet, PlacesViewSet

itinerary_router = DefaultRouter()
itinerary_router.register(r"", ItineraryViewSet)

day_router = DefaultRouter()
day_router.register(r"", DayViewSet)

places_router = DefaultRouter()
places_router.register(r"", PlacesViewSet)


urlpatterns = [
    path("itinerary/", include(itinerary_router.urls)),
    path("itinerary/<int:itinerary_id>/day/", include(day_router.urls)),
    path("place/", include(places_router.urls)),
]
