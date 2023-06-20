from django.urls import path
from . import views

urlpatterns = [
    path("", views.Green_cards_supporters.as_view()),
    path("<int:pk>", views.Green_cards_supporterDetail.as_view()),
]