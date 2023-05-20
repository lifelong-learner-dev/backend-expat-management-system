from django.urls import path
from . import views

urlpatterns = [
    path("", views.Driving_licenses_preparation_documents.as_view()),
    path("<int:pk>", views.Driving_licenses_preparation_documentDetail.as_view()),
]