from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm, UserCreationForm,UserChangeForm

from users.models import User

class UserLoginForm(AuthenticationForm):
    username = forms.CharField()
    password = forms.CharField()


class Meta:
    model = User
    fields = ['username', 'password']

class UserRegistrationForm(UserCreationForm):
    model = User
    fields={
        "username",
        "email",
        "password1",
        "password2",
    }

username = forms.CharField()
email = forms.CharField()
password1 = forms.CharField()
password2 = forms.CharField()

class ProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields={
        "image",
        "username",
        "email",
        }


image = forms.ImageField(required=False)
username = forms.CharField()
email = forms.CharField()

