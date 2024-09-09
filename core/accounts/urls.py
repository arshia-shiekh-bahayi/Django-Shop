from django.urls import path
from .views import Login,Logout,ResetPassword,PasswordResetComplete , PasswordResetConfirm , PasswordResetDone
app_name = 'accounts'

urlpatterns = [
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('password-reset/', ResetPassword.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirm.as_view(),name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetComplete.as_view(),name='password_reset_complete'),
    path('password-reset-done/', PasswordResetDone.as_view(), name='password_reset_done'),

     
]