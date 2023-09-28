from rest_framework import serializers

from helpers.models import Doctor, School, Student, Teacher

# Report
class TeacherSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField()
    class Meta:
        model = Teacher
        depth = 1
        fields = ('name','age' ,'gender','tel', 'email','school')

class SchoolSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(read_only=True, many=True)

    class Meta:
        model = School
        fields = '__all__'
        

        
class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField()
    class Meta:
        model = Student
        fields = ('name','age', 'school', 'stream', 'gender', 'disability')
        # fields = '__all__'

# class ReportSerializer(serializers.ModelSerializer):
#     class Meta:
#         model =Report
#         fields = '__all__'
