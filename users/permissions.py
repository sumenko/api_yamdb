from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class IsYAMDBAdministrator(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == User.Roles.ADMIN
