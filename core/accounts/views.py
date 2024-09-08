from django.contrib.auth import views as auth_views
from django.urls import reverse
from .forms import AuthenticationForm

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