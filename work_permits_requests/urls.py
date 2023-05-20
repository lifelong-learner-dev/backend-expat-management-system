from django.urls import path
from . import views

urlpatterns = [
    path("", views.Work_permits_requests.as_view()),
    path("<int:pk>", views.Work_permits_requestDetail.as_view()),
]