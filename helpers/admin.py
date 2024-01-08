from django.contrib import admin

# Register your models here.
from helpers.models import Doctor, School, Student, Teacher, Case

admin.site.register (Teacher)
admin.site.register(Student)
admin.site.register(School)
admin.site.register(Doctor)
admin.site.register(Case)
