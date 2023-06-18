from django.urls import path
from . import views

urlpatterns = [
    path("", views.Work_permits.as_view()),
    path("<int:pk>", views.Work_permitDetail.as_view()),
    ]