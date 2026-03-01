
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('About_us/', views.About_us, name='About_us'),
    path('Analytic/', views.Analytic, name='Analytic'),
    path('connect/', views.connect, name='connect'),
    path('Design/', views.Design, name='Design'),
    path('Finance/', views.Finance, name='Finance'),
    path('Log_in/', views.Log_in, name='Log_in'),
    path('main/', views.main, name='main'),
    path('Managing/', views.Managing, name='Managing'),
    path('Marketing/', views.Marketing, name='Marketing'),
    path('Programming/', views.Programming, name='Programming'),
    path('Teachers/', views.Teachers, name='Teachers'),
    ]