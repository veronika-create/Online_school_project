from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.list_of_teachers_for_groups, name='index'),
    path('Alist_of_students/', views.list_of_students, name='list_of_students'),
    path('list_of_teachers/', views.list_of_teachers, name='list_of_teachers'),
    path('Massages/', views.Massages, name='Massages'),
    path('results/', views.results, name='results'),

]