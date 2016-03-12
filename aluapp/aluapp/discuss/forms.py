from django import forms

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
        fields = ['title', 'category', 'comment']

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(NewTopicForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['category'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['category'].choices = get_categories()
