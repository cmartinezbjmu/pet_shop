"""Pets urls."""
from django.urls import path, include
from . import views

urlpatterns = [
    path('new/', views.CreatePet, name='create_pet'),
    path('history/', views.historyPet, name='history'),
]
