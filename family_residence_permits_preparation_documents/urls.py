from django.urls import path
from . import views

urlpatterns = [
    path("", views.Family_residence_permits_preparation_documents.as_view()),
    path("<int:pk>", views.Family_residence_permits_preparation_documentDetail.as_view()),
]