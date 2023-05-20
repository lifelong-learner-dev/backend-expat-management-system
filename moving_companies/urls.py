from django.urls import path
from . import views

urlpatterns = [
    path("", views.Moving_companys.as_view()),
    path("<int:pk>", views.Moving_companyDetail.as_view()),
]