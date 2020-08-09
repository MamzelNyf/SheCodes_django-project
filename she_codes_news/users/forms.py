from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    
    class Meta: 
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ['username', 'email']


class ProfileForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', ]
        labels = {
            'username': 'Choose your username:',
            'email': 'Change your email:',

        }
        widgets ={
            'username' : forms.TextInput(
                attrs={
                'class': 'text_field',
                'placeholder' : 'your username',
                }),
            'content' : forms.TextInput(
                attrs={
                    'class': 'text_field',
                    'placeholder' : 'your email',
                }),
            
            }