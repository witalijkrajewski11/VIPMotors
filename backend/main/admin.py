from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from main import models, forms


@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    form = forms.MyUserChangeForm
    add_form = forms.UserCreationForm

    list_display = (
        'email',
        'first_name',
        'last_name',
        'is_confirmed',
        'is_accepted_terms_and_conditions'
    )

    list_filter = (
        'is_confirmed',
    )

    readonly_fields = (
        'date_joined',
        'last_login',
    )

    fieldsets = (
        (None, {'fields': (
            'email', 'username', 'first_name', 'last_name', 'password',
        )}),
        ('Permissions', {'fields': (
            'is_staff', 'is_superuser', 'is_active', 'member_type',
        )}),
        ('Personal info', {'fields': (
            'is_confirmed',
            'is_accepted_terms_and_conditions',
            'date_joined', 'last_login',
            'phone_number',
        )})

    )

