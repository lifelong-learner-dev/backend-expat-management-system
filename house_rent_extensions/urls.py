from django.urls import path
from . import views

urlpatterns = [
    path("", views.House_rent_extension.as_view()),
    path("<int:pk>", views.House_rent_extensionDetail.as_view()),
]