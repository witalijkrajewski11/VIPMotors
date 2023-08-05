from django.apps import apps
from django.conf import settings
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, FileExtensionValidator
from django.db import models
from django.utils import timezone

from main.utils import generate_unique_username
from main import constants


class MyUserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.username = generate_unique_username(user, self.model)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    phone_number = models.CharField(max_length=15)
    is_confirmed = models.BooleanField(default=False)

    is_accepted_terms_and_conditions = models.BooleanField(default=False)

    member_type = models.CharField(
        max_length=15,
        choices=constants.MemberType.choices,
        default=constants.MemberType.member,
    )

    notifications_when = models.CharField(
        choices=constants.NotificationsWhen.choices,
        default=constants.NotificationsWhen.right_now,
        max_length=100,
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = MyUserManager()

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = generate_unique_username(self, User)
        super().save(*args, **kwargs)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'


class ActivationKey(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    key = models.CharField(max_length=8, unique=True)
    is_confirmed = models.BooleanField(default=False)
    expiration_datetime = models.DateTimeField()
