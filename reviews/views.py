from django.shortcuts import get_object_or_404
from rest_framework.permissions import (
    AllowAny, IsAdminUser, IsAuthenticatedOrReadOnly,
)
from rest_framework.viewsets import ModelViewSet

from api.models import Title

from .models import Review
from .serializers import CommentSerializer, ReviewSerializer


class ReviewViewSet(ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly | IsAdminUser]

    def get_queryset(self):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        title = get_object_or_404(Title, id=title_id)
        queryset = title.reviews.all()
        return queryset

    def perform_create(self, serializer):
        title_id = self.request.parser_context['kwargs'].get('title_id')
        title = get_object_or_404(Title, id=title_id)
        serializer.save(title=title)


class CommentViewSet(ModelViewSet):
    serializer_class = CommentSerializer
    # permission_classes = [IsOwnerOrReadonly]
    permission_classes = [AllowAny]

    def get_queryset(self):
        review_id = self.request.parser_context['kwargs'].get('review_id')
        # title_id = self.request.parser_context['kwargs'].get('title_id')
        print('review', review_id)
        review = get_object_or_404(Review, id=review_id)
        queryset = review.comments.all()
        return queryset

    def perform_create(self, serializer):
        review_id = self.request.parser_context['kwargs'].get('review_id')
        review = get_object_or_404(Review, id=review_id)
        # revie/wcomments.
        # FIXME
        serializer.save(author=self.request.user,
                        review_id=review_id,
                        title_id=1)
