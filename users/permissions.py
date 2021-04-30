from django.contrib.auth import get_user_model
from rest_framework import permissions

User = get_user_model()


class IsYAMDBAdministrator(permissions.BasePermission):

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return request.user.role == User.Roles.ADMIN


class IsOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
            print('permission IsOwner for {} on {}'.format(request.user, obj.user))
            # if request.method in permissions.SAFE_METHODS:
            #     return True
            # FIXME:
            return obj.user == request.user and request.user.is_authenticated
