from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Lecturer
from .models import Qrcode
from .models import Post
from .models import Ams
from .models import Unitregister
from django.forms import FileField, Form, ModelForm


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "group", "unit_name", "title", "academic_year"]

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super(UserRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class LecRegister(forms.ModelForm):
    class Meta:
        model = Lecturer
        fields = ["first_name", "second_name", "ID_No", "phone_No", "email", "image_urls", "unit_name", "course_code",
                  "faculty", "group", "academic_year"]
        labels = {'first_name': "First Name", "second_name": "Second Name", "ID_No": "ID", "phone_No": "Phone No",
                  "email": "email", "image_urls": "Image Link", "unit_name":"Unit name", "course_code": "Course Code",
                  'faculty':"School/Faculty", 'group':"Group/Class", 'academic_year':"Academic Year"}


class QrRegister(forms.ModelForm):
    class Meta:
        model = Qrcode
        fields = ["first_name", "second_name", "unit_name", "group_year", "qr_generator", "form_generator", "edit_link", "responses_link", ]
        labels = {'first_name': "First Name", "second_name": "Second Name",'unit_name': "Name of Unit", "group_year": "Group & Year",
                  "qr_generator": "Default-QR: https://chart.googleapis.com/chart?chs=500x500&cht=qr&chl=",
                  "form_generator":"Default Form: https://forms.gle/Luvf5W5C57VhTMZw5 ",
                  "edit_link": "Default edit-Link: https://forms.gle/Luvf5W5C57VhTMZw5",
                  "responses_link": "Default responses: https://forms.gle/Luvf5W5C57VhTMZw5",}


class AmsRegister(ModelForm):
    class Meta:
        model = Ams
        fields = ["timestamp", "email_address", "first_name", "second_name","admission"]


class UploadForm(Form):
    attendance_file = FileField()


class UnitRegister(ModelForm):
    class Meta:
        model = Unitregister
        fields = ["timestamp", "email_address", "first_name", "second_name","admission","unit_name", "group",
                  "lec_first_name", "lec_second_name"]


class UploadRegister(Form):
    register_file = FileField()
