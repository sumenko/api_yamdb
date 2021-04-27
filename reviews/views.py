from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly
)
from rest_framework.viewsets import ModelViewSet

from api.models import Title

from .models import Review
from .serializers import CommentSerializer, ReviewSerializer
from api.permissions import ReviewCommentPermissions


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [ReviewCommentPermissions,
                          IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        serializer.save(author=self.request.user, title=title)

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs.get('title_id'))
        return title.reviews.all()


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly,
                          ReviewCommentPermissions]
    #permission_classes = [AllowAny]

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        serializer.save(author=self.request.user, review=review)

    def get_queryset(self):
        review = get_object_or_404(Review, pk=self.kwargs.get('review_id'))
        return review.comments.all()
