from rest_framework import serializers
from cars import models


class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CarBrand
        fields = '__all__'
