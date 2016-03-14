from django import forms
from django.contrib.auth.models import User

from .models import *
from utils import get_list

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

    def save(self):
        lines = self.cleaned_data['student_list']
        for line in lines:
            index_no, first_name, last_name, email = line.split(',')
            Student.objects.create(index_no=index_no, first_name=first_name, last_name=last_name, email=email)

class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Announcement
        exclude = ['date_created']

    def __init__(self, *args, **kwargs):
        super(AnnouncementForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})

class DocumentRequestForm(forms.ModelForm):
    class Meta:
        model = DocumentRequest
        exclude = ['date_created']

    def __init__(self, *args, **kwargs):
        super(DocumentRequestForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget = forms.TextInput(attrs={'class': 'form-control'})
        self.fields['document_type'].widget = forms.Select(attrs={'class': 'form-control'})
        self.fields['document_type'].label = 'Document Type'
        self.fields['document_type'].choices = get_list(DocumentType)
        self.fields['upload_quantity'].widget = forms.TextInput(attrs={'class': 'form-control'})

""" class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['doc'] """
