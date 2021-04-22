from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('auth_app.urls')),
    path('api/v1/users/', include('users.urls')),
    # path('api/v1/users/', include('users.urls.UsersClass', namespace='auth')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
