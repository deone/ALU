from django import forms
from django.contrib.auth.models import User

from .models import *

def get_categories():
    category_list = [('', 'Select')]

    for category in Category.objects.all():
        tup = (category.id, category.title)
        category_list.append(tup)
        
    return category_list

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewTopicForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['category'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['category'].choices = get_categories()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'topic']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        self.topic = kwargs.pop('topic', None)
        super(CommentForm, self).__init__(*args, **kwargs)
