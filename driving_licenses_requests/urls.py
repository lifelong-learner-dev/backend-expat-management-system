from django.urls import path
from . import views

urlpatterns = [
    path("", views.Driving_licenses_requests.as_view()),
    path("<int:pk>", views.Driving_licenses_requestDetail.as_view()),

]