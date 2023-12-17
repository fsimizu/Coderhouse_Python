from django import forms
from . import models
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel


# class RegisterForm(forms.ModelForm):
#     # first_name = forms.CharField(label="First name", max_length=50)
    
#     class Meta:
#         model = models.User
#         fields = ["first_name", "last_name", "email", "password"]


class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")
    email = forms.EmailField(label="Email")
    username = forms.CharField(label="Username")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repeat password", widget=forms.PasswordInput)

    class Meta:
        model = UserModel
        fields = ["first_name", "last_name", "email", "username", "password1", "password2"]
        help_texts = {k: "" for k in fields}


class UserAvatar(forms.ModelForm):
    class Meta:
        model = models.Avatar
        fields = ["image"]