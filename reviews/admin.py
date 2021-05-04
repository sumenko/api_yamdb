from django.contrib import admin
from import_export.admin import ImportMixin

from titles.models import Category, Genre, Title

from .models import Comment, Review
from .resources import (
    CategoryResource, CommentResource, GenreResource, ReviewResource,
    TitleResource,
)


class ReviewAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'score', 'pub_date', 'title_name')
    resource_class = ReviewResource

    def title_name(self, obj):
        return "{}({})".format(obj.title.name, obj.title.id)


class CommentAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('id', 'review_id', 'author', 'text', 'pub_date',
                    'review_short')
    resource_class = CommentResource

    def review_short(self, obj):
        return "{}({})".format(obj.review.text[:20], obj.review.id)


class CategoryAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('name', 'slug')
    resource_class = CategoryResource


class GenreAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('name', 'slug')
    resource_class = GenreResource


class TitleAdmin(ImportMixin, admin.ModelAdmin):
    list_display = ('id', 'name', 'year', 'category_name',
                    'genre_name')
    resource_class = TitleResource

    def category_name(self, obj):
        return obj.category.name

    def genre_name(self, obj):
        return ', '.join([a.name for a in obj.genre.all()])


admin.site.register(Review, ReviewAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
