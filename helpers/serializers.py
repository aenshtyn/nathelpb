from rest_framework import serializers

from helpers.models import Doctor, School, Student, Teacher

# Report

class SchoolSerializer(serializers.ModelSerializer):

    class Meta:
        model = School
        fields = '__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'

# class ReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Report
#         fields = '__all__'
