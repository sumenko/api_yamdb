from rest_framework.routers import DefaultRouter

from .views import UsersViewset

router = DefaultRouter()
router.register('v1/users', UsersViewset, basename='users')

urlpatterns = []
urlpatterns += router.urls
