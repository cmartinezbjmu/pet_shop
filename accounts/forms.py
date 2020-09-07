"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User


class SignupForm(forms.Form):
    """Sign up form."""
    username = forms.CharField(min_length=4, max_length=50, label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Usuario', 'class': 'form-control', 'required': True, 'style': 'background-color: #65ba68;'}))
    password = forms.CharField(max_length=70, label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña', 'class': 'form-control', 'required': True, 'style': 'background-color: #65ba68;'}))
    password_confirmation = forms.CharField(max_length=70, label=False, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirme su contraseña', 'class': 'form-control', 'required': True, 'style': 'background-color: #65ba68;'}))
    first_name = forms.CharField(min_length=4, max_length=50, label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre', 'class': 'form-control', 'required': True, 'style': 'background-color: #65ba68;'}))
    last_name = forms.CharField(min_length=4, max_length=50, label=False, widget=forms.TextInput(
        attrs={'placeholder': 'Apellido', 'class': 'form-control', 'required': True, 'style': 'background-color: #65ba68;'}))
    email = forms.CharField(min_length=6, max_length=70, label=False, widget=forms.EmailInput(
        attrs={'placeholder': 'Correo electrónco', 'class': 'form-control', 'required': True, 'style': 'background-color: #65ba68;'}))

    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        username_taken = User.objects.filter(username=username).exists()
        if username_taken:
            raise forms.ValidationError('Username is already in use.')
        return username

    def clean(self):
        """Verify password confirmation match."""
        data = super().clean()

        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')
        return data

    def save(self):
        """Create user and ."""
        data = self.cleaned_data
        data.pop('password_confirmation')
        user = User.objects.create_user(**data)
