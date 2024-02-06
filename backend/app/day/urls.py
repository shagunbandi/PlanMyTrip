from attraction import urls as attraction_urls
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import DayMethodView, DayViewSet

router = DefaultRouter()
router.register(r"", DayViewSet)

urlpatterns = [
    path(
        "<int:day_id>/move/<str:method>/",
        DayMethodView.as_view(),
        name="day-method",
    ),
    path("", include(router.urls)),
    path("<int:day_id>/attraction/", include(attraction_urls)),
]
