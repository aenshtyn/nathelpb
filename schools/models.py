from django.db import models

# Create your models here.
class School(models.Model):
    name = models.CharField(blank=False, max_length=80, default='')
    email = models.CharField(blank=False, max_length=80, default='')
    tel = models.CharField(blank=False, max_length=80, default='')
    address = models.CharField(blank=False, max_length=80, default='')
    orientation = models.CharField(blank=False, max_length=80, default='')
    level = models.CharField(blank=False, max_length=80, default='')
    curriculum = models.CharField(blank=False, max_length=80, default='')
    county = models.CharField(blank=False, max_length=80, default='')
    sub_county = models.CharField(blank=False, max_length=80, default='')
    location = models.CharField(blank=False, max_length=80, default='')
    student_population = models.CharField(blank=False, max_length=80, default='')
    teacher_population = models.CharField(blank=False, max_length=80, default='')
