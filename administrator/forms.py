from django import forms
from tinymce.widgets import TinyMCE
from .models import BBIT
from .models import BTC
from .models import ICS
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']


# class UserRegistrationForm(UserCreationForm):
#     email = forms.EmailField(help_text='A valid email address, please.', required=True)
#
#     class Meta:
#         model = get_user_model()
#         fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
#
#     def save(self, commit=True):
#         user = super(UserRegistrationForm, self).save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#         return user


class NewsletterForm(forms.Form):
    subject = forms.CharField()
    receivers = forms.CharField()
    message = forms.CharField(widget=TinyMCE(), label="Email content")


class BbitForm(forms.ModelForm):
    class Meta:
        model = BBIT
        fields = ["first_name", "second_name", "ID_No", "group", "unit_name", "course_code", "academic_year"]
        labels = {'first_name': "First Name", "second_name": "Second Name", "ID_No": "ID", "group": "Class/Group",
                  "unit_name":"Unit name", "course_code": "Course Code", 'academic_year':"Academic Year" }


class BtcForm(forms.ModelForm):
    class Meta:
        model = BTC
        fields = ["first_name", "second_name", "ID_No", "group", "unit_name", "course_code", "academic_year"]
        labels = {'first_name': "First Name", "second_name": "Second Name", "ID_No": "ID", "group": "Class/Group",
                  "unit_name":"Unit name", "course_code": "Course Code", 'academic_year':"Academic Year"}


class IcsForm(forms.ModelForm):
    class Meta:
        model = ICS
        fields = ["first_name", "second_name", "ID_No", "group", "unit_name", "course_code", "academic_year"]
        labels = {'first_name': "First Name", "second_name": "Second Name", "ID_No": "ID", "group": "Class/Group",
                  "unit_name":"Unit name", "course_code": "Course Code", 'academic_year':"Academic Year"}