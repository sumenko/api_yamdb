from django.urls import include, path
from rest_framework.routers import DefaultRouter

# FIXME
from .views import UsersViewset  # OneUserViewSet

router = DefaultRouter()
router.register('', UsersViewset, basename='users')
# router.register('me', UsersViewset, basename='me')

urlpatterns = [
    # path('v1/users/me/', OneUserViewSet.as_view()),
    # path('v1/users/me/', include(router.urls)),
    path('v1/users/', include(router.urls)),
]
