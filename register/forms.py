from django import forms
from django.contrib.auth.forms import UserCreationForm, AdminUserCreationForm
from .models import User, CurrencyChoices

class UserRegistrationForm(UserCreationForm):
    currency = forms.ChoiceField(choices=CurrencyChoices, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'currency', 'password1', 'password2')


class AdminRegistrationForm(AdminUserCreationForm):
    currency = forms.ChoiceField(choices=CurrencyChoices)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'currency', 'password1', 'password2', 'is_superuser')
