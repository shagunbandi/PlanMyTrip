from django.urls import include, path
from itinerary.views.agenda import AgendaViewSet, MoveAgendaView
from itinerary.views.itinerary import ItineraryViewSet
from itinerary.views.place import MovePlaceView, PlaceViewSet
from rest_framework.routers import DefaultRouter

itinerary_router = DefaultRouter()
itinerary_router.register(r"", ItineraryViewSet)

agenda_router = DefaultRouter()
agenda_router.register(r"", AgendaViewSet)


places_router = DefaultRouter()
places_router.register(r"", PlaceViewSet)


urlpatterns = [
    # Itinerary
    path("itinerary/", include(itinerary_router.urls)),
    # Agenda
    path("itinerary/<int:itinerary_id>/agenda/", include(agenda_router.urls)),
    path(
        "itinerary/<int:itinerary_id>/agenda/<int:agenda_id>/move/",
        MoveAgendaView.as_view(),
        name="move-agenda",
    ),
    # Place
    path(
        "itinerary/<int:itinerary_id>/agenda/<int:agenda_id>/place/",
        include(places_router.urls),
    ),
    path(
        "itinerary/<int:itinerary_id>/agenda/<int:agenda_id>/place/<int:place_id>/move/",
        MovePlaceView.as_view(),
        name="move-place",
    ),
]
