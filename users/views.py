from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsYAMDBAdministrator
from .serializers import UserSerializer

User = get_user_model()


class UsersViewset(ModelViewSet):
    # admin, djangoadmin - могут все
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    permission_classes = [IsAdminUser | IsYAMDBAdministrator]

    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'


class OneUserViewSet(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(User, username=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
