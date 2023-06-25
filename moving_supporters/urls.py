from django.urls import path
from . import views

urlpatterns = [
    path("", views.Moving_supporters.as_view()),
    path("<int:pk>", views.Moving_supporterDetail.as_view()),
]