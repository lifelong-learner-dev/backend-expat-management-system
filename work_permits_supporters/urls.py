from django.urls import path
from . import views

urlpatterns = [
    path("", views.Work_permits_supporters.as_view()),
    path("<int:pk>", views.Work_permits_supporterDetail.as_view()),
]