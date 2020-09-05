""""Pet views."""

# Django
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Forms
from .forms import PetForm

# Models
from .models import Pet

# Create your views here.

class CreatePetView(LoginRequiredMixin, CreateView):
    """Create new pet."""

    template_name='pet/create_pet.html'
    form_class = PetForm
    success_url = reverse_lazy('/')

