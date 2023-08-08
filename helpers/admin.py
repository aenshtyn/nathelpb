from django.contrib import admin

# Register your models here.
from helpers.models import Teacher, Student, School, Doctor

admin.site.register (Teacher)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Doctor)
