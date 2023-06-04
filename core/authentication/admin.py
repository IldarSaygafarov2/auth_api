from django.contrib import admin
from .models import CustomUser

# Register your models here.


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ("pk", "username", "first_name", "is_staff")
    list_display_links = ("pk", "username")
