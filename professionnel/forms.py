from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import UserProfil


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class UserProfilForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields = ['profession','commune','quartier','rue','telephone']

class UserSearchForm(forms.ModelForm):
    class Meta:
        model = UserProfil
        fields = ['profession', 'commune', 'quartier']
