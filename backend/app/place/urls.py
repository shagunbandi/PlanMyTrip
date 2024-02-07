from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MovePlaceView, PlaceViewSet

router = DefaultRouter()
router.register(r"", PlaceViewSet)

urlpatterns = [
    path(
        "<int:place_id>/move/<str:method>/",
        MovePlaceView.as_view(),
        name="move-place",
    ),
    path("", include(router.urls)),
]
