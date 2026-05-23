from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    
    
    path('questions/', views.questions, name='questions'),
    
    
]