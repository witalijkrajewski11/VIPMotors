from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import routers

from cars.views import car_views

router = routers.DefaultRouter()
router.register(r'car_brands', car_views.CarBrandViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
