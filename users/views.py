from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAdministrator
from .serializers import UserSerializer

User = get_user_model()

@api_view(['GET',])
def smoke(request):
    user = get_object_or_404(User, username=request.user)
    print(request.user)
    print(user.role)
    return Response('i\'m a teapot', status=status.HTTP_418_IM_A_TEAPOT)

class UsersViewset(ModelViewSet):
    # admin - может все
    # moderator - ? 
    # user - обновить свои данные, получить данные
    # anonymous - не может ничего
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdministrator,)
    # filter_backends = (DjangoFilterBackend,)
    # filterset_fields = ('group', )

    # def perform_create(self, serializer):
    #     return serializer.save(author=self.request.user)
