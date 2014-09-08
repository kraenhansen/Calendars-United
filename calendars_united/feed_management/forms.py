from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django import forms

class CustomAuthenticationForm(AuthenticationForm):
	username = forms.CharField(widget=TextInput(attrs={
		'class': 'form-control',
		'placeholder': 'Username',
		'required': '',
		'autofocus': '',
		}))
	password = forms.CharField(widget=PasswordInput(attrs={'class': 'form-control','placeholder':'Password'}))