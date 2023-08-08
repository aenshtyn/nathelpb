from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser

from helpers.models import Doctor, School, Student, Teacher
from helpers.serializers import SchoolSerializer

# Create your views here.


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
        return JsonRespons({'message': 'School was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
