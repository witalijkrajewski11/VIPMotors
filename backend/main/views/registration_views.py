import os

from django.contrib.auth import get_user_model
from django_registration.exceptions import ActivationError
from django_registration.views import RegistrationView, ActivationView
from django.utils import timezone
from django.conf import settings

from rest_framework.authtoken.models import Token
from rest_framework import mixins, exceptions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import GenericViewSet

from main import emails, models, utils, serializers


User = get_user_model()


class EmailConfirmationView(RegistrationView):
    def send_activation_email(self, user):
        emails.UserConfirmationEmailSender.run(dict(
            to=user,
            member=user,
            activation_key=self.get_activation_key(user),
        ))

    def get_activation_key(self, user):
        key_instance = models.ActivationKey.objects.filter(
            user=user, is_confirmed=False,
            expiration_datetime__gte=timezone.now(),
        ).first()
        if key_instance:
            return key_instance.key

        key = models.User.objects.make_random_password(length=8)
        expiration = timezone.now() + timezone.timedelta(
            days=settings.ACCOUNT_ACTIVATION_DAYS)
        models.ActivationKey.objects.create(
            user=user, key=key, expiration_datetime=expiration)
        return key


class CustomActivationView(ActivationView):
    success_url = f"{os.getenv('FRONTEND_URL')}/email-confirmed"

    def activate(self, *args, **kwargs):
        username = self.validate_key(kwargs.get("activation_key"))
        self.user = self.get_user(username)
        self.user.is_confirmed = True
        self.user.save()
        return self.user

    def validate_key(self, activation_key):
        try:
            key_instance = models.ActivationKey.objects.get(
                key=activation_key, is_confirmed=False,
                expiration_datetime__gte=timezone.now(),
            )
        except models.ActivationKey.DoesNotExist:
            super().validate_key(activation_key)

        key_instance.is_confirmed = True
        key_instance.save()

        return getattr(key_instance.user, User.USERNAME_FIELD)

    def get_success_url(self, user=None):
        success_url = super().get_success_url(user)
        token, created = Token.objects.get_or_create(user=self.user)
        success_url += f'?token={token}'
        return success_url

    def get_user(self, username):
        try:
            user = User.objects.get(**{User.USERNAME_FIELD: username})
            if user.is_confirmed:
                raise ActivationError(
                    self.ALREADY_ACTIVATED_MESSAGE, code="already_activated"
                )
            return user
        except User.DoesNotExist:
            raise ActivationError(self.BAD_USERNAME_MESSAGE, code="bad_username")


class UserCreateViewSet(mixins.CreateModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.ListModelMixin,
                        GenericViewSet,
                        EmailConfirmationView):
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    pagination_class = None

    def filter_queryset(self, queryset):
        qs = super().filter_queryset(queryset)
        if self.request.user.is_authenticated:
            qs = qs.filter(pk=self.request.user.pk)
        else:
            qs = qs.none()
        return qs

    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.UserCreateSerializer
        return serializers.UserSerializer

    def perform_create(self, serializer):
        email = serializer.validated_data['email'].lower()
        terms_and_conditions = serializer.validated_data['is_accepted_terms_and_conditions']
        user = models.User(
            email=email,
            username=email,
            is_accepted_terms_and_conditions=terms_and_conditions
        )
        user.username = utils.generate_unique_username(user, models.User)
        user.set_password(serializer.validated_data['password'])
        user.save()

        self.send_activation_email(user)

    @action(detail=False, methods=['post'])
    def send_confirmation_email(self, request):
        if not request.user.is_authenticated:
            raise exceptions.NotAuthenticated()
        if request.user.is_confirmed:
            return Response({'ok': False, 'error': 'Already confirmed'})
        self.send_activation_email(request.user)
        return Response({'ok': True})


