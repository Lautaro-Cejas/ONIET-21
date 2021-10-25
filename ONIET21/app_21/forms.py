from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserLoginForm(UserCreationForm):
    usuario = forms.CharField()
    psw = forms.CharField(label='Contraseña', widget=forms.PasswordInput)