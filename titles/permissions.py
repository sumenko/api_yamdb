from rest_framework import permissions

from auth_app.models import User

MODERATOR_METHODS = ('PATCH', 'DELETE')


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_admin
                or request.user.is_superuser)

    def has_object_permission(self, request, view, obj):
        return (request.method in permissions.SAFE_METHODS
                or request.user.is_authenticated
                and request.user.is_admin
                or request.user.is_superuser)


class ReviewCommentPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method == 'POST':
            return not request.user.is_anonymous()

        if request.method in MODERATOR_METHODS:
            return (
                request.user == obj.author
                or request.user.is_admin
                or request.user.is_moderator
            )

        return request.method in permissions.SAFE_METHODS
