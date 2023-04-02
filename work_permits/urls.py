from django.urls import path
from . import views

urlpatterns = [
    path("", views.work_permits),
    path("<int:pk>", views.work_permit),
    ]