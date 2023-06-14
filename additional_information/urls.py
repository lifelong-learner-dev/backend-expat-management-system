from django.urls import path
from . import views

urlpatterns = [
    path("", views.Additional_information.as_view()),
    path("<int:pk>", views.Additional_informationDetail.as_view()),
]