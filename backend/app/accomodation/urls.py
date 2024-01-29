from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import AccomodationViewSet, MoveAccomodationView

router = DefaultRouter()
router.register(r"", AccomodationViewSet)

urlpatterns = [
    path(
        "<int:accomodation_id>/move/<str:method>/",
        MoveAccomodationView.as_view(),
        name="move-accomodation",
    ),
    path("", include(router.urls)),
]
