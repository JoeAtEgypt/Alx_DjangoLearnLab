from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = UserAdmin.fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {"fields": ("date_of_birth", "profile_photo")}),
    )
    list_display = UserAdmin.list_display + ("date_of_birth", "profile_photo")
    search_fields = UserAdmin.search_fields + ("date_of_birth",)


admin.site.register(CustomUser, CustomUserAdmin)
