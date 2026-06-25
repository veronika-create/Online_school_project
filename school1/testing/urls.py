
from django.urls import path

from testing import views

app_name = 'testing'

urlpatterns = [
    path('test/', views.test,  name='test'),
   
    path('results/', views.results, name='results'),

	
]

