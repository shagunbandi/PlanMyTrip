from django.urls import include, path
from itinerary.views.agenda import AgendaViewSet
from itinerary.views.itinerary import ItineraryViewSet
from itinerary.views.place import PlaceViewSet
from rest_framework.routers import DefaultRouter

itinerary_router = DefaultRouter()
itinerary_router.register(r"", ItineraryViewSet)

agenda_router = DefaultRouter()
agenda_router.register(r"", AgendaViewSet)

places_router = DefaultRouter()
places_router.register(r"", PlaceViewSet)


urlpatterns = [
    path("itinerary/", include(itinerary_router.urls)),
    path("itinerary/<int:itinerary_id>/agenda/", include(agenda_router.urls)),
    path(
        "place/",
        include(places_router.urls),
    ),
    # path(
    #     "move/<int:object_id>/",
    #     MoveContentView.as_view(),
    # ),
]
