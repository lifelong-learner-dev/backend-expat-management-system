from django.urls import path
from . import views

urlpatterns = [
    path("", views.Green_cards_processes.as_view()),
    path("<int:pk>", views.Green_cards_processDetail.as_view()),
]