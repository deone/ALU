from django import forms

from .models import SimpleComment

class SimpleCommentForm(models.ModelForm):
    class Meta:
        model = SimpleComment
        exclude = ['user']
