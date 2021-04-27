from rest_framework import permissions

from auth_app.models import User
from .models import Roles

MODERATOR_METHODS = ('PATCH', 'DELETE')


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.role == User.Roles.ADMIN
                or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.role == User.Roles.ADMIN
                or request.user.is_superuser)


class ReviewCommentPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return not request.user.is_anonymous()

        if request.method in MODERATOR_METHODS:
            return (
                request.user == obj.author
                or request.user.role == Roles.ADMIN
                or request.user.role == Roles.MODERATOR
            )

        return request.method in permissions.SAFE_METHODS
