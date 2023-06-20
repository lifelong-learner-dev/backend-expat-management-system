from django.urls import path
from . import views

urlpatterns = [
    path("", views.Additional_information_supporters.as_view()),
    path("<int:pk>", views.Additional_information_supporterDetail.as_view()),
]