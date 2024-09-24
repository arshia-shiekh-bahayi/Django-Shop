from django.contrib import admin
from .models import Contact , Newsletter


# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("id","name","subject","phone_number","created_date",)

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ("email",)