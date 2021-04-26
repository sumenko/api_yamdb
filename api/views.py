from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from .filters import TitleFilter
from .mixins import DestroyListCreateViewSet
from .models import Category, Genre, Title
from .permissions import IsAdminOrReadOnly
from .serializers import (
    CategorySerializer, GenreSerializer, TitleListSerializer,
    TitlePostSerializer,
)


class CategoryViewSet(DestroyListCreateViewSet):
    '''апивью для категорий'''
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)


class GenreViewSet(DestroyListCreateViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = 'slug'
    pagination_class = PageNumberPagination
    filter_backends = (filters.SearchFilter,)
    search_fields = ('=name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return TitleListSerializer
        return TitlePostSerializer
