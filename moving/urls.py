from django.urls import path
from . import views

urlpatterns = [
    path("", views.Moving.as_view()),
    path("<int:pk>", views.MovingDetail.as_view()),
    path("explanations/", views.Explanations.as_view()),
    path("explanations/<int:pk>", views.ExplanationDetail.as_view()),
]