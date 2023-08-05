from rest_framework import serializers
from main import models


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)

    class Meta:
        model = models.User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = [
            'email',
            'password',
            'is_accepted_terms_and_conditions'
        ]

