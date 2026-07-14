from django.urls import path

from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.feedback, name='feedback'),
    
    path('stquestions_list/', views.stquestions_list, name='stquestions_list'),
    
    path('questions/', views.questions, name='questions'),
    
    
]