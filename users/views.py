from django.contrib.auth import get_user_model
from rest_framework import filters, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsYAMDBAdministrator
from .serializers import UserSerializer

User = get_user_model()


class UsersViewset(ModelViewSet):
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsYAMDBAdministrator]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(detail=False, methods=['get', 'patch'],
            permission_classes=[IsAuthenticated])
    def me(self, request, pk=None):
        user = User.objects.get(username=request.user)
        if request.method == 'GET':
            serializer = self.get_serializer(user)
        else:
            serializer = self.get_serializer(user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
