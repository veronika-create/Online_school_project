from django.urls import path

from users import views

app_name = "users"

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('registration/', views.registration, name = 'registration'),
    path('profile/', views.profile, name = 'profile'),
    #path('user/accounts/profile/', views.profile, name = 'profile'),
     path('Contacts_of_teachers/', views.Contacts_of_teachers_list, name='Contacts_of_teachers'),
    path('logout/', views.logout, name = 'logout'),
    path('My_students/', views.My_students_list, name='My_students'),
    path('Students/', views.Students_list, name='Students'),
]
