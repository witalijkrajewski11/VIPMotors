from rest_framework.response import Response
from rest_framework import status, mixins
from rest_framework.decorators import action
from rest_framework.viewsets import GenericViewSet

from django.db.models import Q

from cars import models, serializers


class CarBrandViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = models.CarBrand.objects.all()

    def get_serializer_class(self):
        return serializers.CarBrandSerializer

    def filter_queryset(self, queryset):
        return queryset