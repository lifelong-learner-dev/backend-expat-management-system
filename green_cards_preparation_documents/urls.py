from django.urls import path
from . import views

urlpatterns = [
    path("", views.Green_cards_preparation_documents.as_view()),
    path("<int:pk>", views.Green_cards_preparation_documentDetail.as_view()),
]