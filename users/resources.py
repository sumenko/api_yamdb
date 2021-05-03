from django.contrib.auth import get_user_model
from import_export import resources

User = get_user_model()


class UserResource(resources.ModelResource):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'role', 'description',
                  'first_name', 'last_name')
