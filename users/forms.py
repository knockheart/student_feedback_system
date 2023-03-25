from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from .models import Admin


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Admin
        fields = ("email",)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Admin
        fields = ("email",)
