"""Pet forms."""

# Django
from django import forms

# Models
from .models import Pet

class PetForm(forms.ModelForm):
    """"Pet model form."""
    class Meta:
        model = Pet
        fields = ('name', 'pet_type', 'size', 'description')