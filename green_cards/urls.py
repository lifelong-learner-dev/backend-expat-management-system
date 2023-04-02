from django.urls import path
from . import views

urlpatterns = [
    path("", views.Green_cards.as_view()),
    path("<int:pk>", views.Green_cardDetail.as_view()),
    path("explanations/", views.Explanations.as_view()),
    path("explanations/<int:pk>", views.ExplanationDetail.as_view()),
]