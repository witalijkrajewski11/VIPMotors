from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.core.exceptions import ValidationError
import django.db.models

from main import models


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = models.User
        fields = ('email', 'username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class MyUserChangeForm(UserChangeForm):
    class Meta:
        model = models.User
        fields = (
            'email', 'username', 'password', 'is_active', 'is_confirmed',
            'is_staff', 'is_superuser',
            'first_name', 'last_name', 'is_accepted_terms_and_conditions',
            'member_type',

            'phone_number',
        )

    def clean_password(self):
        return self.initial["password"]
