from django.urls import path
from . import views

urlpatterns = [
    path("", views.Pick_ups_requests.as_view()),
    path("<int:pk>", views.Pick_ups_requestDetail.as_view()),
]