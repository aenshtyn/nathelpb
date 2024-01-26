from django.contrib import admin

# Register your models here.
from helpers.models import Doctor, School, Student, Teacher, Case, Condition

admin.site.register (Teacher)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Doctor)
admin.site.register(Case)
admin.site.register(Condition)
