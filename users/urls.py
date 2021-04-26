from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import OneUserViewSet, UsersViewset

router = DefaultRouter()
# router.register('me', OneUserViewSet, basename='oneuser')
router.register('', UsersViewset, basename='users')

urlpatterns = [
    path('me/', OneUserViewSet.as_view()),
    path('', include(router.urls)),
]
