from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from helpers.models import Doctor, School, Student, Teacher, Doctor, Case
from helpers.serializers import SchoolSerializer, TeacherSerializer, StudentSerializer, DoctorSerializer

import datetime
from datetime import timedelta
from django.utils import timezone

# Create your views here.




# SCHOOLS

@api_view(['GET', 'POST', 'DELETE'])
def school_list(request):
    if request.method == 'GET':
        schools = School.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            schools = schools.filter(name__icontains=name)
        schools_serializer =  SchoolSerializer(schools, many=True)
        return JsonResponse(schools_serializer.data, safe=False)


    elif request.method == 'POST':
        school_data = JSONParser().parse(request)
        school_serializer = SchoolSerializer(data=school_data)
        if school_serializer.is_valid():
            school_serializer.save()
        return JsonResponse(school_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(school_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def school_details(request, pk):

    try:
        school = School.objects.get(pk=pk)
    except School.DoesNotExist:
        return JsonResponse({'messsage': 'The School does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        school_serializer = SchoolSerializer(school)
        return JsonResponse(school_serializer.data)

    elif request.method == 'PUT':
        school_data =  JSONParser(). parse(request)
        school_serializer =  SchoolSerializer(school, data= school_data)
        if school_serializer.is_valid():
            school_serializer.save()
            return JsonResponse(school_serializer.data)
        return JsonResponse(school_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        school.delete()
        return JsonResponse({'message': 'School was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

# STUDENTS

@api_view(['GET', 'POST', 'DELETE'])
def student_list(request):
    if request.method == 'GET':
        students = Student.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            students = students.filter(name__icontains=name)
        students_serializer =  StudentSerializer(students, many=True)
        return JsonResponse(students_serializer.data, safe=False)


    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
        return JsonResponse(student_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def student_details(request, pk):

    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return JsonResponse({'messsage': 'The Student does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        student_serializer = StudentSerializer(student)
        return JsonResponse(student_serializer.data)

    elif request.method == 'PUT':
        student_data =  JSONParser(). parse(request)
        student_serializer =  StudentSerializer(student, data= student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse(student_serializer.data)
        return JsonResponse(student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return JsonResponse({'message': 'Student was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def student_count(request, format=None):
    student_count = Student.objects.count()
    return student_count
# TEACHERS

@api_view(['GET', 'POST', 'DELETE'])
def teacher_list(request):
    if request.method == 'GET':
        teachers = Teacher.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            teachers = teachers.filter(name__icontains=name)
        teachers_serializer =  TeacherSerializer(teachers, many=True)
        return JsonResponse(teachers_serializer.data, safe=False)


    elif request.method == 'POST':
        teacher_data = JSONParser().parse(request)
        teacher_serializer = TeacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
        return JsonResponse(teacher_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(teacher_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def teacher_details(request, pk):

    # try:
        
        return JsonResponse

# DOCTORS

@api_view(['GET', 'POST', 'DELETE'])
def doctor_list(request):
    if request.method == 'GET':
        doctors = Doctor.objects.all()

        name = request.GET.get('name', None)
        if name is not None:
            doctors = doctors.filter(name__icontains=name)
        doctors_serializer =  DoctorSerializer(doctors, many=True)
        return JsonResponse(doctors_serializer.data, safe=False)


    elif request.method == 'POST':
        doctor_data = JSONParser().parse(request)
        doctor_serializer = DoctorSerializer(data=doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
        return JsonResponse(doctor_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST', 'DELETE'])
def doctor_details(request, pk):

    try:
        doctor = Doctor.objects.get(pk=pk)
    except Doctor.DoesNotExist:
        return JsonResponse({'messsage': 'The Doctor does not exist'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        doctor_serializer = DoctorSerializer(doctor)
        return JsonResponse(doctor_serializer.data)

    elif request.method == 'PUT':
        doctor_data =  JSONParser(). parse(request)
        doctor_serializer =  DoctorSerializer(doctor, data= doctor_data)
        if doctor_serializer.is_valid():
            doctor_serializer.save()
            return JsonResponse(doctor_serializer.data)
        return JsonResponse(doctor_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        doctor.delete()
        return JsonResponse({'message': 'Doctor was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    

@api_view(['GET'])
def helper_analytics(request):

    total_helpers = Student.objects.all().count()
    total_schools = School.objects.all().count()
    total_teachers = Teacher.objects.all().count()


    
 # Calculate date ranges
    today = timezone.now()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)

 # Get weekly and monthly new additions
    weekly_new_student_additions =  Student.objects.filter(date_joined__range=(last_week, today)).count()    
    monthly_new_student_additions = Student.objects.filter(date_joined__range=(last_month, today)).count()
    monthly_new_school_additions = School.objects.filter(date_joined__range=(last_month, today)).count()
    monthly_new_teacher_additions =Teacher.objects.filter(date_joined__range=(last_month, today)).count()


# Prepare data to be returned as JSON

    data = {
        'total_helpers': total_helpers,
        'total_teachers': total_teachers,
        'total_schools': total_schools,
        'weekly_new_student_additions': weekly_new_student_additions,
        'monthly_new_student_additions': monthly_new_student_additions,
        'monthly_new_school_additions': monthly_new_school_additions,
        'monthly_new_teacher_additions': monthly_new_teacher_additions,
    }

    return JsonResponse(data)


@api_view(['GET'])
def case_analytics(request):

    # Count total cases
    total_cases = Case.objects.all().count()

    # Calculate date ranges
    today = timezone.now()
    last_week = today - timedelta(days=7)
    last_month = today - timedelta(days=30)

    # Get weekly and monthly cases
    weekly_cases = Case.objects.filter(date_reported__range=(last_week, today)).count()
    monthly_cases = Case.objects.filter(date_reported__range=(last_month, today)).count()

    # Calculate percentage change for weekly cases
    # previous_week_cases = Case.objects.filter(date_reported__range=(last_week - timedelta(days=7), last_week)).count
    # percentage_change = 0.0
    # if previous_week_cases != 0:
    #     percentage_change = ((weekly_cases - previous_week_cases) / previous_week_cases) * 100

    data = {
        'total_cases': total_cases,
        'weekly_cases': weekly_cases,
        'monthly_cases': monthly_cases,
        # 'percentage_change': percentage_change
    }

    return JsonResponse(data)
