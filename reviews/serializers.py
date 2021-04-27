from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment, Review

User = get_user_model()


class ReviewSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    author = serializers.ReadOnlyField(source='author.username')

    def validate(self, data):
        title_id = self.context.get('view').kwargs.get('title_id')
        author = self.context.get('request').user
        if (self.context.get('request').method == 'POST'
                and Review.objects.filter(title_id=title_id,
                                          author_id=author.id).exists()):
            raise serializers.ValidationError(
                'Вы уже оставили отзыв на данное произведение')
        return data

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField()
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment