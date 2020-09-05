"""Pets models."""

# Django
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pet(models.Model):
    """Pet model."""

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    name = models.CharField(max_length=50, blank=False)
    pet_type = models.CharField(max_length=10, blank=False)
    size = models.CharField(max_length=10, blank=False)
    description = models.TextField(blank=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)