from django.urls import path
from . import views

urlpatterns = [
    path("", views.Driving_licenses_processes.as_view()),
    path("<int:pk>", views.Driving_licenses_processDetail.as_view()),
]