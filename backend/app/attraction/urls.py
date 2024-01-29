from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AttractionViewSet, MoveAttractionView

router = DefaultRouter()
router.register(r"", AttractionViewSet)

urlpatterns = [
    path("/", include(router.urls)),
    path(
        "<int:day_id>/<int:attraction_id>/move/<str:method>/",
        MoveAttractionView.as_view(),
        name="move-attraction",
    ),
]
