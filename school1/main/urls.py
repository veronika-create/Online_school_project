
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:subjects_slug>', views.About_us, name='About_us'),
    #path('<slug:subjects_slug>', views.Log_in, name='Log_in'),
    #path('main/', views.main, name='main'),
    #path('<slug:subjects_slug>/', views.Subjects_all, name='Subjects_all'),
    #path('connect/', views.connect, name='connect'),
    path('<slug:subjects_slug>/', views.Design, name='Design'),
    path('<slug:subjects_slug>/', views.Finance, name='Finance'),
    path('<slug:subjects_slug>/', views.Managing, name='Managing'),
    path('<slug:subjects_slug>/', views.Marketing, name='Marketing'),
    path('<slug:subjects_slug>/', views.Programming, name='Programming'),
    path('<slug:subjects_slug>/', views.Teachers, name='Teachers'),
    ]