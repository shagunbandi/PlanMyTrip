from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AttractionViewSet, MoveAttractionView

router = DefaultRouter()
router.register(r"", AttractionViewSet)

urlpatterns = [
    path(
        "<int:day_id>/<int:attraction_id>/move/<str:method>/",
        MoveAttractionView.as_view(),
        name="move-attraction",
    ),
    path("<int:day_id>", include(router.urls)),
]
