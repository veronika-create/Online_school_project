from django.urls import path
from feedback import views

app_name = 'feedback'

urlpatterns = [
    path('feedback/', views.FeedbackView.as_view, name='feedback'),
    
]