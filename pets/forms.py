"""Pet forms."""

# Django
from django import forms

# Models
from .models import Pet

class PetForm(forms.ModelForm):
    """"Pet model form."""
    class Meta:
        model = Pet
        fields = ['name', 'pet_type', 'size', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control form-field', 'placeholder': 'Nombre de la mascota', 'label': ''}),
            'pet_type': forms.Select(attrs={'class': 'form-control form-field-select form-field', 'placeholder': 'Tipo de mascota'}),
            'size': forms.RadioSelect(attrs={'class': 'form-control form-field form-field-radio form-check-inline', 'placeholder': 'Tamaño'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-field', 'placeholder': 'Descripción'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label = ''
        self.fields['pet_type'].label = ''
        self.fields['size'].label = ''
        self.fields['size'].empty_label = None
        self.fields['description'].label = ''
        self.fields['size'].widget.choices = [('Pequeno', 'Pequeño'), ('Medio', 'Medio'), ('Grande', 'Grande')]
        #import pdb; pdb.set_trace()
        #user = kwargs.pop('user', None)
        #self.fields['user'] = user