from django.urls import path
from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.Messages, name='feedback'),
    
    path('questions/', views.feedback, name='questions'),
    
    
]