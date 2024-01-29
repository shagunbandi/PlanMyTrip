from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DayMethodView, DayViewSet

router = DefaultRouter()
router.register(r"", DayViewSet)

urlpatterns = [
    path(
        "<int:itinerary_id>/<int:day_id>/move/<str:method>/",
        DayMethodView.as_view(),
        name="day-method",
    ),
    path("<int:itinerary_id>/", include(router.urls)),
]
