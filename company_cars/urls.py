from django.urls import path
from . import views

urlpatterns = [
    path("", views.Company_cars.as_view()),
    path("<int:pk>", views.Company_carDetail.as_view()),
]