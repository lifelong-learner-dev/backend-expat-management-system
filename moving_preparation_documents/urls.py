from django.urls import path
from . import views

urlpatterns = [
    path("", views.Moving_preparation_documents.as_view()),
    path("<int:pk>", views.Moving_preparation_documentDetail.as_view()),
]