from django.urls import path
from . import views

urlpatterns = [
    path("", views.Moving.as_view()),
    path("<int:pk>", views.MovingDetail.as_view()),
]