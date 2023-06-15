from django.urls import path
from . import views

urlpatterns = [
    path("", views.Family_residence_permits_requests.as_view()),
    path("<int:pk>", views.Family_residence_permits_requestDetail.as_view()),
]