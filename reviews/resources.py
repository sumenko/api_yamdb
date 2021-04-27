from import_export import resources

from reviews.models import Comment, Review
from titles.models import Category, Genre, Title


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
