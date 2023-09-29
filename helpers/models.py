import datetime

from django.db import models
from django.utils import timezone

DISABILITY = [
    ("NONE", "None"),
    ("BLIND", "Vision Impairment"),
    ("DEAF", "Hard of Hearing"),
    ("AUTISM", "Autism"),
    ("PHYSICAL IMPAIRMENT", "Physical Impairment"),
    ( "COGNITIVE", "Cognitive Impairment"),
    ( "PSYCHOLOGICAL","Psychological Impairment"),
]

GENDER = [
    ("Male", "Male"),
    ("Female", "Female"),
] 
class NameMixin:
    @property
    def name(self):
        return f'{self.first_name} {self.last_name}'
    
class AgeMixin:
    @property
    def age(self):
        return timezone.now().year - self.dob.year 
    
class Doctor(NameMixin, AgeMixin, models.Model):
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, default='')
    email = models.CharField(blank=False, max_length=80, default='')
    tel = models.CharField(blank=False, max_length=80, default='')


    def __str__(self):
       return '{} {}'.format(self.first_name, self.last_name)


class Issue(models.Model):
    name = models.CharField(blank=False, max_length=80, default='')

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
    student_population = models.IntegerField
    teacher_population = models.IntegerField

    def __str__(self):
       return '{}'.format(self.name)


class Teacher(NameMixin, AgeMixin, models.Model):
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, default='')
    email = models.CharField(blank=False, max_length=80, default='')
    tel = models.CharField(blank=False, max_length=80, default='')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
       return '{} {}'.format(self.first_name, self.last_name)
    

class Student(NameMixin, AgeMixin, models.Model):  
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, choices = GENDER, default='')
    disability = models.CharField(max_length= 20, choices = DISABILITY, default = 'none')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade= models.IntegerField
    stream = models.CharField(blank=False, max_length=80, default='')
    uid = models.IntegerField


# class Report(models.Model):
#     date = models.DateField
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     students = models.ForeignKey(School, on_delete=models.CASCADE)


# class Training(models.Model):
#     name = models.CharField(blank=False, max_length=80, default='')
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     students = models.ManyToManyField(Student)
