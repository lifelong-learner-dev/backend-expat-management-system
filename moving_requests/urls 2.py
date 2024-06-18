from django.urls import path
from . import views

urlpatterns = [
    path("", views.Moving_requests.as_view()),
    path("<int:pk>", views.Moving_requestDetail.as_view()),
]