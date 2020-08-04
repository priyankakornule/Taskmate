from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomRegisterForm(UserCreationForm):
    firstname=forms.CharField()
    lastname=forms.CharField()
    email=forms.EmailField()
    

    class Meta:
        model=User
        fields=['username','firstname','lastname','email','password1','password2']