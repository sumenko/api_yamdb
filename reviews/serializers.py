from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Review

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=(serializers.CurrentUserDefault()))

    class Meta:
        model = Review
        fields = ['id', 'author', 'text', 'score', 'pub_date']

    def validate(self, data):
        request = self.context['request']
        if request.method == 'POST':
            print(data)
            author = data['author']
            title_id = request.parser_context['kwargs'].get('title_id')
            if (Review.objects.filter(title_id=title_id,
                                      author=author).exists()):
                raise serializers.ValidationError('Уже есть отзыв')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all(),
        default=(serializers.CurrentUserDefault()))
    title_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ['id', 'title_id', 'review_id', 'text', 'author', 'pub_date']
