from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UsersViewset  # OneUserViewSet

router = DefaultRouter()
router.register('', UsersViewset, basename='users')

urlpatterns = [
    path('v1/users/', include(router.urls)),
]
