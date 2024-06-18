from django.urls import path
from . import views

urlpatterns = [
    path("", views.Real_estate_agents.as_view()),
    path("<int:pk>", views.Real_estate_agentDetail.as_view()),
]