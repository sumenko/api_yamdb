from import_export import resources

from .models import User


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'description',
                  'first_name', 'last_name')
