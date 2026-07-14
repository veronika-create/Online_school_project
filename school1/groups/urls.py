from django.urls import path

from groups import views

app_name = "groups"

urlpatterns = [
    path('courses/', views.courses_list, name='courses'),
    path('groups/', views.groups_list, name='groups'),
    path('My_groups/', views.My_groups_list, name='My_groups'),
    path('My_courses/', views.My_courses_list, name='My_courses'),
    

]