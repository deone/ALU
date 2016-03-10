from django import forms
from django.contrib.auth.models import User

from .models import UserType

class UserTypeForm(forms.Form):
    user_type = forms.ChoiceField(choices=UserType.TYPE_CHOICES, widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(UserTypeForm, self).__init__(*args, **kwargs)

    def save(self):
        user = User.objects.get(username__iexact=self.user.username)
        user_type = UserType.objects.create(user=user, user_type=self.cleaned_data['user_type'])
        user_type.save()

class ImportForm(forms.Form):
    student_list = forms.FileField(label='Student List')
