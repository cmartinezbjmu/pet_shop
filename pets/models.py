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

SERVICE_CHOICES = [
    ('1', 'Cita medica'),
    ('2', 'Cita Vacunación'),
    ('3', 'Cita de desparasitación'),
    ('4', 'Cita de baño'),
    ('5', 'Cita de corte de pelo')
]

class MedicalServices(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='pet_medical_service')

    service_type = models.CharField(max_length=10, blank=False, choices=SERVICE_CHOICES)
    date = models.DateTimeField(verbose_name='fecha', null=True, blank=True)
    
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)