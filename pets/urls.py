"""Pets urls."""
from django.urls import path, include
from . import views

urlpatterns = [
    path('new/', views.CreatePet, name='create_pet'),
    path('history/', views.historyPet, name='history'),
    path('meet/', views.meet, name='meet'),
    path('new_meet/', views.new_meet, name='new_meet'),
    path('edit_meet/<id_meet>/', views.edit_meet, name='edit_meet'),
    path('delete_meet/<id_meet>/', views.delete_meet, name='delete_meet'),
]
