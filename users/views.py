from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .permissions import IsAdministrator
from .serializers import UserSerializer

User = get_user_model()

# TODO list/detail
class UsersViewset(ModelViewSet):
    # admin - может все
    # moderator - ? 
    # user - обновить свои данные, получить данные
    # anonymous - не может ничего
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAdministrator,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    # https://stackoverflow.com/questions/18645175/django-rest-framework-object-level-permissions
    # def perform_create(self, serializer):
    #     return serializer.save(author=self.request.user)
