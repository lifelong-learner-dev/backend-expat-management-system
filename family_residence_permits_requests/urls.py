from django.urls import path
from . import views

urlpatterns = [
    path("", views.Family_residence_permits_requests.as_view()),
    path("<int:pk>", views.Family_residence_permits_requestDetail.as_view()),
    path("explanations/", views.Explanations.as_view()),
    path("explanations/<int:pk>", views.ExplanationDetail.as_view()),
    path("documents/", views.Documents.as_view()),
    path("documents/<int:pk>", views.DocumentDetail.as_view()),
]