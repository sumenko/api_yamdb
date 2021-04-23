from auth_app.models import User
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio',
                  'email', 'role')
        
        model = User

        
