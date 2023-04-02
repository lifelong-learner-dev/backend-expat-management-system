from django.urls import path
from . import views

urlpatterns = [
    path("", views.Green_cards_requests.as_view()),
    path("<int:pk>", views.Green_cards_requestDetail.as_view()),
    path("available_countries/", views.Available_countries.as_view()),
    path("available_countries/<int:pk>", views.Available_countryDetail.as_view()),
]