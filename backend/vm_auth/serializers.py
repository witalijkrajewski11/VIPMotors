from django.contrib.auth import authenticate
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer


class CustomTokenSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get('username') or attrs.get('email')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('No active account found with the given credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        attrs['user'] = user
        return attrs
