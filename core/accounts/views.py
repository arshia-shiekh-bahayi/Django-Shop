from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.shortcuts import redirect
from .forms import AuthenticationForm
from django.urls import reverse_lazy as _
from django.contrib.auth.views import PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin

class Login(auth_views.LoginView):
    template_name = 'accounts/login.html'
    form_class = AuthenticationForm
    redirect_authenticated_user = True
    def get_default_redirect_url(self):
        return reverse('website:index')

class Logout(auth_views.LogoutView):
    # template_name = 'accounts/logout.html'
    def get_default_redirect_url(self):
        return reverse('website:index')
    
class ResetPassword(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."

    success_url = _('accounts:password_reset_done')
    
    
class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    success_url =  _('accounts:password_reset_complete')
    
class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'
    
class PasswordResetDone (auth_views.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'
    