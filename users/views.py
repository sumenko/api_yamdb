from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import filters, generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .permissions import IsYAMDBAdministrator
from .serializers import UserSerializer

User = get_user_model()


# TODO list/detail
class UsersViewset(ModelViewSet):
    # admin - может все
    # moderator - ? 
    # user - обновить свои данные, получить данные
    # anonymous - не может ничего
    queryset = User.objects.all().order_by('username')
    serializer_class = UserSerializer
    # permission_classes = (IsAuthenticated,) # IsYAMDBAdministrator,)
    # permission_classes = (IsYAMDBAdministrator,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'


class OneUserViewSet(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    # lookup_field = 'username'

    def get_object(self):
        print(self.request.user)
        return get_object_or_404(User, username=self.request.user)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
