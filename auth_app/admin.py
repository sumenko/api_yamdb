from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportMixin

from .resources import UserResource

User = get_user_model()


class UserAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'role', 'confirmation_code',
                    'first_name', 'last_name', 'bio', 'is_staff')
    resource_class = UserResource


admin.site.register(User, UserAdmin)
