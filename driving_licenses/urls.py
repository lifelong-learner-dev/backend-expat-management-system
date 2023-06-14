from django.urls import path
from . import views

urlpatterns = [
    path("", views.Driving_licenses.as_view()),
    path("<int:pk>", views.Driving_licenseDetail.as_view()),

]