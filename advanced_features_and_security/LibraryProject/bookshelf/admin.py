from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Book, CustomUser


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
    list_filter = ("author", "publication_year")
    search_fields = ("title", "author")


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

# ---
# To programmatically create groups and assign permissions, run the following in Django shell:
#
# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from bookshelf.models import Book
#
# # Get permissions
# perms = Permission.objects.filter(content_type=ContentType.objects.get_for_model(Book))
# can_view = perms.get(codename='can_view')
# can_create = perms.get(codename='can_create')
# can_edit = perms.get(codename='can_edit')
# can_delete = perms.get(codename='can_delete')
#
# # Create groups
# editors, _ = Group.objects.get_or_create(name='Editors')
# viewers, _ = Group.objects.get_or_create(name='Viewers')
# admins, _ = Group.objects.get_or_create(name='Admins')
#
# # Assign permissions
# editors.permissions.set([can_view, can_create, can_edit])
# viewers.permissions.set([can_view])
# admins.permissions.set([can_view, can_create, can_edit, can_delete])
#
# print('Groups and permissions set up!')
