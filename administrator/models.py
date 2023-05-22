from django.db import models
from django.utils import timezone


class Email(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

class Timetable(models.Model):
    monday = models.CharField(max_length=255)
    time = models.TimeField()
    tuesday = models.CharField(max_length=255)
    time = models.TimeField()
    wednesday = models.CharField(max_length=255)
    time = models.TimeField()
    thursday = models.CharField(max_length=255)
    time = models.TimeField()
    friday = models.CharField(max_length=255)
    time = models.TimeField()


class BBIT(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    ID_No = models.IntegerField()
    group = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=255)


class BTC(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    ID_No = models.IntegerField()
    group = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=255)


class ICS(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    ID_No = models.IntegerField()
    group = models.CharField(max_length=255)
    unit_name = models.CharField(max_length=255)
    course_code = models.CharField(max_length=255)
    academic_year = models.CharField(max_length=255)





