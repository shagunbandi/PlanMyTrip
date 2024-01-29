"""
URL configuration for planmytrip_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from accomodation import urls as accomodation_urls
from attraction import urls as attraction_urls
from day import urls as day_urls
from dish import urls as dish_urls
from django.contrib import admin
from django.urls import include, path
from itinerary import urls as itinerary_urls
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from restaurant import urls as restaurant_urls

urlpatterns = [
    # Auth
    path("admin/", admin.site.urls),
    path("api/token/", TokenObtainPairView.as_view()),
    path("api/token/refresh/", TokenRefreshView.as_view()),
    path("api/token/verify/", TokenVerifyView.as_view()),
    # App
    path("api/itinerary/", include(itinerary_urls)),
    path("api/day/", include(day_urls)),
    path("api/dish/", include(dish_urls)),
    path("api/accomodation/", include(accomodation_urls)),
    path("api/restaurant/", include(restaurant_urls)),
    path("api/attraction/", include(attraction_urls)),
]
