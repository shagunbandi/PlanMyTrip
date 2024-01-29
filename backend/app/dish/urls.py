from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DishViewSet, MoveDishView

router = DefaultRouter()
router.register(r"", DishViewSet)

urlpatterns = [
    path(
        "<int:day_id>/<int:dish_id>/move/<str:method>/",
        MoveDishView.as_view(),
        name="move-dish",
    ),
    path("<int:day_id>/", include(router.urls)),
]