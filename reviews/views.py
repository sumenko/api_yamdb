from api.models import Title
from django.db.models import fields
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from .models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('id', )  # чтобы искать по ID ревью

    def get_queryset(self):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        title = get_object_or_404(Title, id=title_id)
        queryset = title.reviews.all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(author=self.request.user, title_id=title)
