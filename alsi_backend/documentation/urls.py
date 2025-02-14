from django.urls import path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view_instance = get_schema_view(
    openapi.Info(
        title="CMS ALSI Global LLc Documentation",
        default_version='v1',
        description="API documentation for ALSI",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('swagger/', schema_view_instance.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view_instance.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
