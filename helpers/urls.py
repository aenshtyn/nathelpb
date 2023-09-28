from django.urls import path

from helpers import views

urlpatterns = [

    # schools
    
    path("api/schools", views.school_list, name='schools'),
    path("api/schools/<int:pk>/", views.school_details, name='schools_detail'),
    
    # students
    path("api/students", views.student_list, name='students'),
    path("api/students/<int:pk>/", views.student_details, name='students_detail'),

    
    # teachers
    path("api/teachers", views.teacher_list, name='teachers'),
    path("api/teachers/<int:pk>/", views.teacher_details, name='teachers_detail'),

    # doctor
    path("api/doctors", views.doctor_list, name='doctors'),
    path("api/doctors/<int:pk>/", views.teacher_details, name='doctors_detail'),

    
]