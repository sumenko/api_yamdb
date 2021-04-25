from api.models import Category, Genre, Title
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'score', 'pub_date')
    resource_class = Review


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    resource_class = Category


class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    resource_class = Genre


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'rating', 'category_name', 'genre_name')
    resource_class = Title


    def category_name(self, obj):
        return obj.category.name

    def genre_name(self, obj):
        return ', '.join([a.name for a in obj.genre.all()])


admin.site.register(Review, ReviewAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
