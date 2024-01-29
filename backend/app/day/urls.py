from accomodation import urls as accomodation_urls
from attraction import urls as attraction_urls
from dish import urls as dish_urls
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from restaurant import urls as restaurant_urls

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
    path("<int:day_id>/accomodation/", include(accomodation_urls)),
    path("<int:day_id>/attraction/", include(attraction_urls)),
    path("<int:day_id>/dish/", include(dish_urls)),
    path("<int:day_id>/restaurant/", include(restaurant_urls)),
]
