from rest_framework import serializers
# from rest_framework/validators
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        validators = [
            serializers.UniqueTogetherValidator(
                queryset=User.objects.all(),
                fields=['email', 'username'],
                message='Сочетание email-username уже занято'
            )
            ]