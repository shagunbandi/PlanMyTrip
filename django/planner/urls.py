from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.PlanOverview, name='plan-overview'),
]
