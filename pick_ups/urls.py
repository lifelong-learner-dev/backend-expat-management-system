from django.urls import path
from . import views

urlpatterns = [
    path("", views.Pick_ups.as_view()),
    path("<int:pk>", views.Pick_upDetail.as_view()),
    path("explanations/", views.Explanations.as_view()),
    path("explanations/<int:pk>", views.ExplanationDetail.as_view()),
]