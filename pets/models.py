"""Pets models."""

# Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

TYPE_CHOICES = [
    ('', 'Tipo de mascota'),
    ('Gato', 'Gato'),
    ('Perro', 'Perro'),
    ('Pez', 'Pez'),
    ('Otro', 'Otro'),
]

SIZE_CHOICES = [
    ('Pequeno', 'Pequeño'),
    ('Medio', 'Medio'),
    ('Grande', 'Grande')
]

class Pet(models.Model):
    """Pet model."""

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pet')

    name = models.CharField(max_length=50, blank=False)
    pet_type = models.CharField(max_length=10, blank=False, choices=TYPE_CHOICES)
    size = models.CharField(max_length=10, blank=False, choices=SIZE_CHOICES)
    description = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)