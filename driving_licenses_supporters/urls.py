from django.urls import path
from . import views

urlpatterns = [
    path("", views.Driving_licenses_supporters.as_view()),
    path("<int:pk>", views.Driving_licenses_supporterDetail.as_view()),
]