from django.urls import path

from .views import get_confirmation_code, get_token

urlpatterns = [
    path('v1/auth/email/', get_confirmation_code),
    path('v1/auth/token/', get_token),
]
