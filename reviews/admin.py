from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'text', 'score', 'pub_date')
    resource_class = Review


admin.site.register(Review, ReviewAdmin)
