from django.urls import path
from . import views

urlpatterns = [
    path("", views.Family_residence_permits.as_view()),
    path("<int:pk>", views.Family_residence_permitDetail.as_view()),

]