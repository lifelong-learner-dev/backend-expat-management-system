from django.urls import path
from . import views

urlpatterns = [
    path("", views.Driving_licenses_requests.as_view()),
    path("<int:pk>", views.Driving_licenses_requestDetail.as_view()),
    path("explanations/", views.Explanations.as_view()),
    path("explanations/<int:pk>", views.ExplanationDetail.as_view()),
    path("documents/", views.Documents.as_view()),
    path("documents/<int:pk>", views.DocumentDetail.as_view()),
    path("visit_places/", views.Visit_places.as_view()),
    path("visit_places/<int:pk>", views.Visit_placeDetail.as_view()),

]