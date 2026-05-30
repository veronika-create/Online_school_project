
from django.urls import path

from testing import views

app_name = 'testing'

urlpatterns = [
	path('tests/', views.tests,  name='tests'),
    path('results/', views.results, name='results'),
	
]