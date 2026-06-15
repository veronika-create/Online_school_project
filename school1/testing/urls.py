
from django.urls import path

from testing import views

app_name = 'testing'

urlpatterns = [
    path('test/', views.tests,  name='test'),
    #path('<int:question_id>/grade/', views.test, name='test'),
    path('results/<int:test_id>/', views.test_results, name='test_results'),

	
]
#