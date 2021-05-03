# from rest_framework/validators
from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()
    email = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['username', 'email']
        # FIXME
        # validators = [
        #     serializers.UniqueTogetherValidator(
        #         queryset=User.objects.all(),
        #         fields=['email', 'username'],
        #         message='Сочетание email-username уже занято')]
    def validate(self, data):
        print('code_validation')
        print(data['username'])
        return data
