from rest_framework import permissions


class IsYAMDBAdministrator(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):    
    #     # if request.method in permissions.SAFE_METHODS:
    #     #     return True
    #     return False
        print(request.user)
        print(request.user.role)

        return request.user.role == 'admin'  # FIXME

    def has_permission(self, request, view):
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        print(request.user)
        print(request.user.role)
        return request.user.role == 'admin'  # FIXME
        
        # return super().has_permission(request, view)
