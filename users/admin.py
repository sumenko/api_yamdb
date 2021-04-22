from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from import_export.admin import ImportMixin

from .models import User
from .resources import UserResource


class UserAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('username', 'email', 'role', 'confirmation_code',
                    'first_name', 'last_name', 'description')
    resource_class = UserResource

admin.site.register(User, UserAdmin)
