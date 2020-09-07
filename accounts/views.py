from django.shortcuts import render
from django.views.generic import FormView
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy

# Forms
from accounts.forms import SignupForm

class SignupView(FormView):
    """Users signup view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('accounts:login')

    def form_valid(self, form):
        """Save from data."""
        form.save()
        return super().form_valid(form)

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'
    redirect_authenticated_user = True

class LogoutView(auth_views.LogoutView):
    """Logout view."""
    pass