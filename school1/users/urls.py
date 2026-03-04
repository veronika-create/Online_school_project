from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('about_us_adm/', views.about_us_adm, name = 'about_us_adm'),
    path('Help_admin/', views.Help_admin, name = 'Help_admin'),
    path('Ivanov/', views.Ivanov, name = 'Ivanov'),
    path('list_of_students/', views.list_of_students, name = 'list_of_students'),
    path('list_of_teachers_for_groups/', views.list_of_teachers_for_groups, name = 'list_of_teachers_for_groups'),
    path('Massages/', views.Massages, name = 'Massages'),
    path('List_of_teachers/', views.List_of_teachers, name = 'List_of_teachers'),
    path('Pilipenko/', views.Pilipenko, name = 'Pilipenko'),
    path('profile_admin/', views.profile_admin, name = 'profile_admin'),
    path('registed_users/', views.registed_users, name = 'registed_users'),

]