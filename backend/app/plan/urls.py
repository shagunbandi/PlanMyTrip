from django.urls import include, path
from plan.views.agenda import AgendaViewSet, MoveAgendaView
from plan.views.place import MovePlaceView, PlaceViewSet
from plan.views.plan import PlanViewSet
from rest_framework.routers import DefaultRouter

plan_router = DefaultRouter()
plan_router.register(r"", PlanViewSet)

agenda_router = DefaultRouter()
agenda_router.register(r"", AgendaViewSet)


places_router = DefaultRouter()
places_router.register(r"", PlaceViewSet)


urlpatterns = [
    # Plan
    path("plan/", include(plan_router.urls)),
    # Agenda
    path("plan/<int:plan_id>/agenda/", include(agenda_router.urls)),
    path(
        "plan/<int:plan_id>/agenda/<int:agenda_id>/move/",
        MoveAgendaView.as_view(),
        name="move-agenda",
    ),
    # Place
    path(
        "plan/<int:plan_id>/agenda/<int:agenda_id>/place/",
        include(places_router.urls),
    ),
    path(
        "plan/<int:plan_id>/agenda/<int:agenda_id>/place/<int:place_id>/move/",
        MovePlaceView.as_view(),
        name="move-place",
    ),
]
