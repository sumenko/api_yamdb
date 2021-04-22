from django.urls import path

from .views import get_confirmation_code, get_token

urlpatterns = [
    path('email/', get_confirmation_code),
    path('token/', get_token),
]
