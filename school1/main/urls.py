
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('About_us/', views.About_us, name='About_us'),
    path('Log_in/', views.Log_in, name='Log_in'),

    #path('<slug:slug>/', views.Subjects_all, name='Subjects_all'),
    #path('main/', views.main, name='main'),
    #path('Subjects_all/<slug:subjects_slug>/', views.Subjects_all, name='Subjects_all'),
    path('<slug:subjects_slug>/', views.Subjects_all, name='Subjects_all'),
    #path('Subjects_all/', views.Subjects_all, name='Subjects_all'),
    #path('connect/', views.connect, name='connect'),
    #path('<slug:subjects_slug>/', views.Design, name='Design'),
    #path('<slug:subjects_slug>/', views.Finance, name='Finance'),
    #path('<slug:subjects_slug>/', views.Managing, name='Managing'),
    #path('<slug:subjects_slug>/', views.Marketing, name='Marketing'),
    #path('<slug:subjects_slug>/', views.Programming, name='Programming'),
    path('Teachers/', views.Teachers, name='Teachers'),
    ]