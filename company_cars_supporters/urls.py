from django.urls import path
from . import views

urlpatterns = [
    path("", views.Company_cars_supporters.as_view()),
    path("<int:pk>", views.Company_cars_supporterDetail.as_view()),
]