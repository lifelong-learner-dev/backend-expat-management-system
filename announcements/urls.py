from django.urls import path
from . import views

urlpatterns = [
    path("", views.Announcements.as_view()),
    path("<int:pk>", views.AnnouncementDetail.as_view()),
]