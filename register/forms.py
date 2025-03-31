from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User, CurrencyChoices

class UserRegistrationForm(UserCreationForm):
    currency = forms.ChoiceField(choices=CurrencyChoices, required=True)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'currency', 'password1', 'password2')

class UserLoginForm(AuthenticationForm):
    pass
