from django.urls import path
from . import views

urlpatterns = [
    path("", views.Work_permits_processes.as_view()),
    path("<int:pk>", views.Work_permits_processDetail.as_view()),
]