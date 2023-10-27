from django.urls import path
from . import views

urlpatterns = [
    path("", views.fetch_compound, name="fetch-compound"),
    path("all/", views.fetch_all_compound, name="fetch-all-compound"),
    path("create/", views.create_compound, name="create-compound"),
]
