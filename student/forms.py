from django import forms
from .models import Registration, Search
from tinymce.widgets import TinyMCE
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User



class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2', 'first_name','last_name',]


class MyForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ["first_name", "second_name", "ID_No"]
        labels = {"first_name": "First Name", "second_name": "Last Name", "ID_No": "ID Number"}

class SearchCourse(forms.ModelForm):
    class Meta:
        model = Search
        fields = ["unit_name", "admission"]
        labels = {"unit_name": "Search Unit", "admission": "Admission Number"}