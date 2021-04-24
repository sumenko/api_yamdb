from api.models import Title
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Review

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          queryset=User.objects.all(),
                                          default=(
                                            serializers.CurrentUserDefault())
                                          )
    # title_id = serializers.SlugRelatedField(slug_field='id',
    #                                         queryset=Title.objects.all(),
    #                                         read)

    class Meta:
        fields = ['id', 'title_id', 'author', 'text', 'score', 'pub_date']

        model = Review
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'title_id'],
                message='Вы уже оставили отзыв.')
        ]
