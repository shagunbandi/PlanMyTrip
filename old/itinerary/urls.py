from day import urls as day_urls
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ItineraryViewSet

router = DefaultRouter()
router.register(r"", ItineraryViewSet)

urlpatterns = [
    # Your other URL patterns
    path("", include(router.urls)),  # Include the router's URL patterns
    path("<int:itinerary_id>/day/", include(day_urls)),
]
