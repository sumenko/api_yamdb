# from rest_framework/validators
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ['email', 'username']


class UserConfirmationSerializer(UserAuthSerializer):
    confirmation_code = serializers.CharField(max_length=100,
                                              allow_blank=False,
                                              required=True)

    class Meta:
        model = User
        fields = ['confirmation_code', 'email', 'username']
