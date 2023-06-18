from django.urls import path
from . import views

urlpatterns = [
    path("", views.Family_residence_permits_processes.as_view()),
    path("<int:pk>", views.Family_residence_permits_processDetail.as_view()),
]