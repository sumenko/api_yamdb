from api.models import Title
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Review

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    # author = serializers.SlugRelatedField(slug_field='username',
    #                                       queryset=User.objects.all(),
    #                                       default=(
    #                                         serializers.CurrentUserDefault())
    #                                       )
    author = serializers.PrimaryKeyRelatedField(read_only=True, default=serializers.CurrentUserDefault())
    # title_id = serializers.IntegerField(read_only=True)
    # FIXME
    # title_id = serializers.SlugRelatedField(slug_field='Title.id',
    #                                         #queryset=Title.objects.all(),
    #                                         read_only=True)

    class Meta:
        fields = ['id', 'author', 'text', 'score', 'pub_date']

        model = Review
        # FIXME
        # validators = [
        #     UniqueTogetherValidator(
        #         queryset=Review.objects.all(),
        #         fields=['author', 'title_id'],
        #         message='Вы уже оставили отзыв.')
        # ]
