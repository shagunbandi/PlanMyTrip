from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AttractionViewSet

router = DefaultRouter()
router.register(r"", AttractionViewSet)

urlpatterns = [
    # Your other URL patterns
    path("api/", include(router.urls)),  # Include the router's URL patterns
]
