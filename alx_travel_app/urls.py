from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
    title='Alx Travel Application',
    default_version='v1',
    description='This documentation covers the APIs used in the ALX travel application.',
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('listings.urls')),
    path('users/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='documentation'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='redoc-documentation'),
]
