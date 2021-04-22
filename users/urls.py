from django.urls import path

from .views import smoke

urlpatterns = [
    path('', smoke),
]
