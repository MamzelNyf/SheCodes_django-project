from django import forms
from django.forms import ModelForm
from .models import NewsStory

class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'content', 'image']
        labels = {
            'title': 'Story Title:',
            # 'author': 'Your name :',
            'pub_date': 'Publication Date',
            'content': 'Your story:',
            'image': 'Your image url',
        }
        widgets ={
            'title' : forms.TextInput(
                attrs={
                'class': 'text_field',
                'placeholder' : 'Story Title',
                }),
            # 'author' : forms.TextInput(
            #     attrs={
            #     'class': 'text_field',
            #     'placeholder' : 'Your name',
            #     }),
            'content' : forms.Textarea(
                attrs={
                    'class': 'text_field',
                    'placeholder' : 'Write your story here',
                    'size': '40'}),
            'pub_date': forms.DateInput(
                format=('%m/%d/%Y'),
                attrs={
                    'class': 'form-control text_field',
                    'placeholder': 'Select a date',
                    'type': 'date',
                }),          
            'image': forms.URLInput(
                attrs={
                    'placeholder': 'Add the Url of your image',
                    'class': 'text_field',

                })
            
        }
        