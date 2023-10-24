from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DayViewSet

router = DefaultRouter()
router.register(r"", DayViewSet)

urlpatterns = [
    # Your other URL patterns
    path("api/", include(router.urls)),  # Include the router's URL patterns
]
