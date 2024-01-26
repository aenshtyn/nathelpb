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
        today = timezone.now()
        dob = self.dob

        years = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        months = today.month - dob.month - (today.day < dob.day)

        if months < 0: months += 12 
        years -= 1
        age_str = ''
        if years > 0:
            age_str += f'{years} {"year" if years == 1 else "years"}'
            if months > 0:
                age_str += ' '
        if months > 0:
            age_str += f'{months} {"month" if months == 1 else "months"}'

        if not age_str:
            age_str = "less than a month"

        return age_str

        # return{'years': years, 'months':÷÷ months}
        # return timezone.now().year - self.dob.year 
    
class Doctor(NameMixin, AgeMixin, models.Model):
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, default='')
    email = models.CharField(blank=False, max_length=80, default='')
    tel = models.CharField(blank=False, max_length=80, default='')


    def __str__(self):
       return f'{self.name}'
    
    class Meta: 
        ordering = ['first_name', 'last_name']

class Condition(models.Model):
    name = models.CharField(blank=False, max_length=80, default='')
    description = models.CharField(blank=False, max_length=200, default='')

    def __str__(self):
       return '{}'.format(self.name)

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
    student_population = models.IntegerField()
    teacher_population = models.IntegerField()
    date_joined = models.DateField()

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
    date_joined = models.DateField()

    def __str__(self):
       return f'{self.name}'
    
    class Meta: 
        ordering = ['first_name', 'last_name']
    

class Student(NameMixin, AgeMixin, models.Model):  
    first_name = models.CharField(blank=False, max_length=80, default='')
    last_name = models.CharField(blank=False, max_length=80, default='')
    dob = models.DateField()
    gender = models.CharField(blank=False, max_length=80, choices = GENDER, default='')
    disability = models.CharField(max_length= 20, choices = DISABILITY, default = 'none')
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    grade= models.IntegerField()
    stream = models.CharField(blank=False, max_length=80, default='')
    uid = models.IntegerField()
    date_joined = models.DateField()

    def __str__(self):
       return f'{self.name}'
    
    class Meta: 
        ordering = ['first_name', 'last_name']


class Case(models.Model):
    condition = models.ForeignKey(Condition, on_delete=models.CASCADE, default='')
    helper = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_reported = models.DateField()
    date_solved = models.DateField()

    def __str__(self):
        return f'{self.condition}'

# class Report(models.Model):
#     date = models.DateField
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     students = models.ForeignKey(School, on_delete=models.CASCADE)


# class Training(models.Model):
#     name = models.CharField(blank=False, max_length=80, default='')
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     students = models.ManyToManyField(Student)
