from django.urls import path
from . import views

urlpatterns = [
    path("", views.Green_cards.as_view()),
    path("<int:pk>", views.Green_cardDetail.as_view()),
]