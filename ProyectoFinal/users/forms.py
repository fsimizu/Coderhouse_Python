from django import forms
from . import models

class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        email = forms.CharField(label="Your email", max_length=100)
        password = forms.CharField(label="Password", max_length=50)
        fields = ["email", "password"]

class RegisterForm(forms.ModelForm):
    class Meta:
        model = models.User
        # first_name = forms.CharField(label="First name", max_length=50)
        fields = ["first_name", "last_name", "email", "password"]
