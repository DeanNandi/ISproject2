from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=255)

    def __str__(self):
        return self.title + "\n" + self.description

class Lecturer(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    ID_No = models.IntegerField()
    phone_No = models.IntegerField()
    email = models.CharField(max_length=255)
    faculty = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=255)
    image_urls = models.CharField(max_length=2083)


class Qrcode(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    group_year = models.CharField(max_length=255)
    qr_generator = models.CharField(max_length=20083)
    form_generator = models.CharField(max_length=20083)
    edit_link = models.CharField(max_length=20083)
    responses_link = models.CharField(max_length=2083)

class Ams(models.Model):
    timestamp = models.CharField(max_length=2555)
    email_address = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    admission = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)

class Unitregister(models.Model):
    timestamp = models.CharField(max_length=2555)
    email_address = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    admission = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    lec_first_name = models.CharField(max_length=255)
    lec_second_name = models.CharField(max_length=255)