from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from django.views.static import serve

from rest_framework import authentication
from rest_framework.schemas import get_schema_view


from vm_auth.views import CustomAuthToken

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('main.urls')),
    path('api/', include('cars.urls')),
    path('api/token/', CustomAuthToken.as_view(), name='simple_token_obtain'),
    path('openapi', get_schema_view(
        title="PBM",
        description="API for all things …",
        version="1.0.0",
        authentication_classes=[
            authentication.SessionAuthentication,
            authentication.BasicAuthentication,
        ],
    ), name='openapi-schema'),
    path('swagger-ui/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='swagger-ui'),
    path('redoc/', TemplateView.as_view(
        template_name='redoc.html',
        extra_context={'schema_url': 'openapi-schema'}
    ), name='redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
