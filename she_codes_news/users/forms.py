from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser, Profile
from django.forms import ModelForm


class CustomUserCreationForm(UserCreationForm):
    
    class Meta: 
        model = CustomUser
        fields = ['username', 'email']

class CustomUserChangeForm(ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email']
        exclude = ['password2', 'password1']

        labels = {
            'username': 'Choose your username:',
            'email': 'Update your email:'
        }
        widgets ={
            'username' : forms.TextInput(
                attrs={
                'class': 'text_field',
                'placeholder' : 'your username',
                }),
            'email' : forms.TextInput(
                attrs={
                    'class': 'text_field',
                    'placeholder' : 'your email',
                }),
        }
        

class ProfileUpdateForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['avatar', 'bio', 'location', 'birth_date']
        labels = {
            'birth_date': 'Update your date of birth:',
            'avatar': 'Choose your profile picture:',
            'bio': 'Update your bio',
            'location': 'Where do you write from?',
        }
        widgets ={
            'birth_date': forms.DateInput(
                # format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control text_field',
                    'type': 'date',
                }),         
                'avatar' :forms.FileInput,
            }