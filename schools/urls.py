from django.urls import path
from schools import views

urlpatterns = [
    path("api/schools", views.school_list, name='schools'),
    path("api/schools/<int:pk>/", views.school_details, name='schools_detail'),
    # path("api/schools/(?P<pk>[0-9]+)$', views.school_detail),
    
]