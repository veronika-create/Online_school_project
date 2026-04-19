
from django.urls import path

from testing import views

app_name = 'testing'

urlpatterns = [
	path('tests/', views.tests,  name='tests'),
    path('add/', views.test_add, name='add'),
    path('edit/<int:poll_id>/choice/add/', views.test_add, name='test_add'),
    path('edit/choice/<int:choice_id>/', views.test_edit, name='test_edit'),
    path('delete/test/<int:test_id>/',views.test_delete, name='test_delete'),

	
]