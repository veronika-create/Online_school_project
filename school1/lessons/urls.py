from django.urls import path

from lessons import views

app_name = "lessons"

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us_std/', views.about_us_std, name='about_us_std'),
    path('Cookie/', views.Cookie, name='Cookie'),
    path('History/', views.History, name='History'),
    path('Massyvy/', views.Massyvy, name='Massyvy'),
    path('Methods/', views.Methods, name='Methods'),
    path('MySQL_in_PHP/', views.MySQL_in_PHP, name='MySQL_in_PHP'),
    path('Obgects/', views.Obgects, name='Obgects'),
    path('Profile_std/', views.Profile_std, name='Profile_std'),
    path('Syntacsis', views.Syntacsis, name='Syntacsis'),

]