from django.urls import path

from groups import views

app_name = "groups"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about_us_prep/', views.about_us_prep, name = 'about_us_prep'),
    path('base_of_knowledge/', views.base_of_knowledge, name = 'base_of_knowledge'),
    path('Courses/', views.Courses, name = 'Courses'),
    path('Groups/', views.Groups, name = 'Groups'),
    path('Help_prep/', views.Help_prep, name = 'Help_prep'),
    path('Lectures/', views.Lectures, name = 'Lectures'),
    path('material_for_students/', views.material_for_students, name = 'material_for_students'),
    path('profile_prep/', views.profile_prep, name = 'profile_prep'),
    path('results/', views.results, name = 'results'),
    path('Tests/', views.Tests, name = 'Tests'),

]