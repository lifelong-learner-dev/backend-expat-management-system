from django.urls import path
from . import views

urlpatterns = [
    path("", views.Houses.as_view()),
    path("<int:pk>", views.HouseDetail.as_view()),
    path("clauses/", views.Clauses.as_view()),
    path("clauses/<int:pk>", views.ClauseDetail.as_view()),
    path("explanations/", views.Explanations.as_view()),
    path("explanations/<int:pk>", views.ExplanationDetail.as_view()),
    path("regulations/", views.Regulations.as_view()),
    path("regulations/<int:pk>", views.RegulationDetail.as_view()),

]