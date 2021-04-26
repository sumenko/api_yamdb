from import_export import resources

from api.models import Category, Genre, Title
from reviews.models import Comment, Review


# FIXME
# Exception Value:
# 'Review' object has no attribute 'get_user_visible_fields'
class TitleResource(resources.ModelResource):
    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'category')


class ReviewResource(resources.ModelResource):
    class Meta:
        model = Review
        fields = ('id', 'title_id', 'text', 'author', 'score', 'pub_date')


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category
        fields = ('id', 'name', 'slug')


class CommentResource(resources.ModelResource):
    class Meta:
        model = Comment
        fields = ('id', 'name', 'slug')


class GenreResource(resources.ModelResource):
    class Meta:
        model = Genre
        fields = ('id', 'name', 'slug')
