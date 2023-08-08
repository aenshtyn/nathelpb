from django.db import models
import datetime


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

        
   

class Doctor(models.Model):
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField(("Date"), default=datetime.date.today)
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


class Teacher(models.Model):
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, default='')
    email = models.CharField(blank=False, max_length=80, default='')
    tel = models.CharField(blank=False, max_length=80, default='')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
       return '{} {}'.format(self.first_name, self.last_name)
    

class Student(models.Model):  
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, choices = GENDER, default='')
    disability = models.CharField(max_length= 20, choices = DISABILITY, default = 'none')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade= models.IntegerField
    stream = models.CharField(blank=False, max_length=80, default='')
    uid = models.IntegerField

    def __str__(self):
       return '{} {}'.format(self.first_name, self.last_name)


# class Report(models.Model):
#     date = models.DateField
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     students = models.ForeignKey(School, on_delete=models.CASCADE)


# class Training(models.Model):
#     name = models.CharField(blank=False, max_length=80, default='')
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     students = models.ManyToManyField(Student)
