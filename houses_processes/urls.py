from django.urls import path
from . import views

urlpatterns = [
    path("", views.Houses_processes.as_view()),
    path("<int:pk>", views.Houses_processDetail.as_view()),
]