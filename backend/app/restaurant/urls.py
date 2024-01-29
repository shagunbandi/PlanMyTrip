from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import MoveRestaurantView, RestaurantViewSet

router = DefaultRouter()
router.register(r"", RestaurantViewSet)

urlpatterns = [
    path(
        "<int:restaurant_id>/move/<str:method>/",
        MoveRestaurantView.as_view(),
        name="move-restaurant",
    ),
    path("", include(router.urls)),
]
