from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AttractionViewSet, MoveAttractionView

router = DefaultRouter()
router.register(r"", AttractionViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path(
        "<int:day_id>/<int:attraction_id>/move/<str:method>/",
        MoveAttractionView.as_view(),
        name="move-dish",
    ),
]
