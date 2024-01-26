from django.urls import path

from helpers import views

urlpatterns = [

    # schools
    
    path("schools", views.school_list, name='schools'),
    path("schools/<int:pk>", views.school_details, name='schools_detail'),
    
    # students
    path("students", views.student_list, name='students'),
    path("students/<int:pk>/", views.student_details, name='students_detail'),

    
    # teachers
    path("teachers", views.teacher_list, name='teachers'),
    path("teachers/<int:pk>/", views.teacher_details, name='teachers_detail'),

    # doctor
    path("doctors", views.doctor_list, name='doctors'),
    path("doctors/<int:pk>/", views.teacher_details, name='doctors_detail'),
    
    # analytics
    path("analytics", views.analytics, name='analytics'),
    # path("analytics/cases", views.case_analytics, name='case_analytics'),

    #  cases
    path("conditions", views.condition_list, name='conditions'),
    path("conditions/<int:pk>", views.condition_details, name='condition_detail'),


    
]