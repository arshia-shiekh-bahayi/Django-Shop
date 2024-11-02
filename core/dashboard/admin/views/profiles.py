from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.views.generic import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from dashboard.permissions import HasAdminAccessPermission
from django.contrib.auth import views as auth_views
from dashboard.admin.forms import AdminPasswordChangeForm, AdminProfileEditForm
from django.contrib.messages.views import SuccessMessageMixin
from accounts.models import Profile
from django.contrib import messages

# Create your views here.

class AdminSecurityEditView(
    LoginRequiredMixin,
    HasAdminAccessPermission,
    SuccessMessageMixin,
    auth_views.PasswordChangeView,):
    template_name = "dashboard/admin/profile/security-edit.html"
    form_class = AdminPasswordChangeForm
    success_url = reverse_lazy("dashboard:admin:security-edit")
    success_message = "بروز رسانی پسورد با موفقیت انجام شد"
    def form_invalid(self, form):        
        messages.error(self.request,"ناموفق")
        return redirect(self.success_url)

class AdminProfileEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    template_name = "dashboard/admin/profile/profile-edit.html"
    form_class = AdminProfileEditForm
    success_url = reverse_lazy("dashboard:admin:profile-edit")
    success_message = "بروز رسانی پروفایل با موفقیت انجام شد"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)

class AdminProfileImageEditView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    http_method_names = ["post"]
    model = Profile
    fields = [
        "image"
    ]
    success_url = reverse_lazy("dashboard:admin:profile-edit")
    success_message = "بروز رسانی تصویر پروفایل با موفقیت انجام شد"

    def get_object(self, queryset=None):
        return Profile.objects.get(user=self.request.user)
    def form_invalid(self, form):
        messages.error(self.request,"ارسال تصویر با مشکل مواجه شد. لطفا مجدد بررسی و تلاش نمایید")
        return redirect(self.success_url)
