from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.memeAPI.as_view()),
    path('<int:pk>/', views.memeAPI.as_view()),
]