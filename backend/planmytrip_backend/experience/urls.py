from django.urls import path
from .views import ExperienceListApiView, ExperienceDetailApiView

urlpatterns = [
    path("api/", ExperienceListApiView.as_view()),
    path("api/<int:experience_id>/", ExperienceDetailApiView.as_view()),
]
