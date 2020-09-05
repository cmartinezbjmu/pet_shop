"""Pets urls."""
from django.urls import path, include
from . import views

urlpatterns = [
    path('new/', views.CreatePetView.as_view(), name='create_pet'),
]
