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
        fields = ['username', 'email', 'birth_date', 'image']
        labels = {
            'username': 'Choose your username:',
            'email': 'Change your email:',
            'birth_date': 'Update your date of birth:',
            'image': 'Choose your profile picture:',
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
            'birth_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control text_field',
                    'placeholder': 'Select a date',
                    'type': 'date',
                }),          
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Add the Url of your profile picture',
                    'class': 'text_field',
                }),
            }