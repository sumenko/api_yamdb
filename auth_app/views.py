from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from api_yamdb.settings import DEFAULT_FROM_EMAIL

from .serializer import UserAuthSerializer, UserConfirmationSerializer

User = get_user_model()


@api_view(['POST', ])
@permission_classes([permissions.AllowAny, ])
def get_confirmation_code(request):
    """ POST Отправляет код подтверждения на почту в параметре email """
    user_serializer = UserAuthSerializer(data=request.data)
    user_serializer.is_valid(raise_exception=True)
    user_mail = user_serializer.validated_data['email']
    username = user_serializer.validated_data['username']

    confirmation_code = User.objects.make_random_password()
    user, _ = User.objects.get_or_create(username=username, email=user_mail)
    user.confirmation_code = confirmation_code
    user.save()

    send_mail('Getting access',
              (f'Dear user!\nTo get access YaMDB use this '
               f'confirmation code: {confirmation_code}'),
              DEFAULT_FROM_EMAIL, [user_mail, ], fail_silently=False)
    return Response(status=status.HTTP_200_OK)


@api_view(['POST', ])
@permission_classes([permissions.AllowAny, ])
def get_token(request):
    """ Получение токена по связке email+confirmation_code """
    user_serializer = UserConfirmationSerializer(data=request.data)
    user_serializer.is_valid(raise_exception=True)
    user = get_object_or_404(User,
                             email=user_serializer.validated_data['email'],
                             username=(
                                 user_serializer.validated_data['username']))

    # код истек или уже использован
    if user.confirmation_code == '':
        return Response({'errors': 'confirmation_code expired'},
                        status=status.HTTP_400_BAD_REQUEST)

    if user.confirmation_code == (
            user_serializer.validated_data['confirmation_code']):
        refresh = RefreshToken.for_user(user)
        user.confirmation_code = ''
        user.save()
        data = {'token': str(refresh.access_token)}
        return Response(data, status=status.HTTP_200_OK)

    return Response({'errors', 'Wrong confirmation code'},
                    status=status.HTTP_400_BAD_REQUEST)
