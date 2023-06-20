from django.urls import path
from . import views

urlpatterns = [
    path("", views.Houses_supporters.as_view()),
    path("<int:pk>", views.Houses_supporterDetail.as_view()),
]