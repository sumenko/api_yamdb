from api.models import Title
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Comment, Review

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          queryset=User.objects.all(),
                                          default=(
                                            serializers.CurrentUserDefault())
                                         )
    title_id = serializers.PrimaryKeyRelatedField(read_only=True,
                                                  default=1)

    class Meta:
        model = Review
        fields = ['id', 'title_id', 'author', 'text', 'score', 'pub_date']

        # FIXME
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'title_id'],
                message='Вы уже оставили отзыв.')
        ]

    def to_representation(self, obj):
        values = super(ReviewSerializer, self).to_representation(obj)
        values.pop('title_id')
        return values


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          queryset=User.objects.all(),
                                          default=(
                                            serializers.CurrentUserDefault())
                                         )
    

    class Meta:
        model = Comment
        fields = ['id', 'title_id', 'review_id', 'text', 'author', 'pub_date']
        pass
