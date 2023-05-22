from django.forms import ModelForm
from django import forms
from .models import Timetable


class UploadForm(ModelForm):
    monday = forms.TextInput()
    tuesday = forms.TextInput()
    wednesday = forms.TextInput()
    thursday = forms.TextInput()
    friday = forms.TextInput()

    class Meta:
        model = Timetable
        fields = ['monday', 'tuesday', 'wednesday']

