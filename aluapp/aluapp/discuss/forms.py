from django import forms
from django.contrib.auth.models import User

from .models import *
from utils import get_list

class NewTopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        super(NewTopicForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['category'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['category'].choices = get_list(Category)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'topic']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
