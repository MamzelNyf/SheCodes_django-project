from django import forms
from django.forms import ModelForm
from .models import NewsStory, Category
from django.db.utils import OperationalError, ProgrammingError

def categoryList():
    try: 
        choices = Category.objects.all().values_list('name', 'name')
        # select box needs double name to work
        choice_list=[]
        for item in choices:
            choice_list.append(item)
        return choice_list
    except (OperationalError, ProgrammingError): 
        return []


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'pub_date', 'category', 'content', 'image']
        labels = {
            'title': 'Story Title:',
            # 'author': 'Your name :',
            'pub_date': 'Publication Date',
            'content': 'Your story:',
            'image': 'Your image url',
        }
        widgets ={
            'title' : forms.TextInput(
                attrs={'class': 'text_field','placeholder' : 'Story Title',}),
            'category': forms.Select(
                choices=categoryList(), 
                # choices has to be befor attrs
                attrs={'class': 'select'}),
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
        }
class UpdateStoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'content', 'image']
        labels = {
            'title': 'Story Title:',
            'content': 'Your story:',
            'image': 'Upload a new image',

        }
        widgets ={
            'title' : forms.TextInput(
                attrs={
                'class': 'text_field',
                'placeholder' : 'Story Title',
                }),
            'content' : forms.Textarea(
                attrs={
                    'class': 'text_field',
                    'placeholder' : 'Write your story here',
                    'size': '40'}),
        }
        
class AddCategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        labels = {
            'name': 'Your category:',
        }
        widgets ={
            'name' : forms.TextInput(
                attrs={
                'class': 'text_field',
                }),
        }

