
from django.urls import path

from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('About_us/', views.About_us, name='About_us'),
    path('Log_in/', views.Log_in, name='Log_in'),
    path('Teachers/', views.Teachers, name='Teachers'),
    path('<slug:subjects_slug>/', views.SubjectsDetailView.as_view(), name='Subjects_all'),
    ]