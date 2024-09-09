from django.contrib.auth import forms as auth_forms
from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import PasswordResetForm as PasswordResetFormCore

class AuthenticationForm(auth_forms.AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AuthenticationForm,self).confirm_login_allowed(user)

        # if not user.is_verified:
        #     raise ValidationError("user is not verified") 
