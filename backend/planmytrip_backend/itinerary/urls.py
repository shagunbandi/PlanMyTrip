from django.urls import path
from .views import ItineraryListApiView, ItineraryDetailApiView

urlpatterns = [
    path("api", ItineraryListApiView.as_view()),
    path("api/<int:itinerary_id>/", ItineraryDetailApiView.as_view()),
]
