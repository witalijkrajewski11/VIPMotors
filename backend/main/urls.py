from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers

from main.views import registration_views

router = routers.DefaultRouter()
router.register(r'users', registration_views.UserCreateViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path(
        "activate/complete/",
        TemplateView.as_view(
            template_name="django_registration/activation_complete.html"),
        name="django_registration_activation_complete",
    ),
    path(
        "activate/<str:activation_key>/",
        registration_views.CustomActivationView.as_view(),
        name="django_registration_activate",
    ),

]
