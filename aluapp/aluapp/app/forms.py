from django import forms

from .models import UserType

class UserTypeForm(forms.Form):
    user_types = forms.ChoiceField(choices=UserType.TYPE_CHOICES, widget=forms.RadioSelect)
