from django.urls import path
import testing as views

app_name = 'testing'

urlpatterns = [
	path('tests/', views.tests,  name='tests'),
	
]