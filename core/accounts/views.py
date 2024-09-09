from django.contrib.auth import views as auth_views
from django.urls import reverse
from .forms import AuthenticationForm
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth import get_user_model

User = get_user_model()

class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    def get_default_redirect_url(self):
        return reverse('website:index')

class LogoutView(auth_views.LogoutView):
    # template_name = 'accounts/logout.html'
    def get_default_redirect_url(self):
        return reverse('website:index')