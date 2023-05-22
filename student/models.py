from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    ID_No = models.IntegerField()
    email = models.CharField(max_length=255)
    course_enrolled = models.CharField(max_length=255)


class Registration(models.Model):
    first_name = models.CharField(max_length=255)
    second_name = models.CharField(max_length=255)
    ID_No = models.IntegerField()


class Search(models.Model):
    unit_name = models.CharField(max_length=255)
    admission = models.CharField(max_length=255)




