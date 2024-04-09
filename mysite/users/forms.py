from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

'''
RegisterForm inherits UserCreationForm & adds additional
field to inbuilt form
'''
class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
