from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'users/index.html')

def about_us_adm(request):
    return render(request, 'users/about_us_adm.html')

def Help_admin(request):
    return render(request, 'users/Help_admin.html')

def Ivanov(request):
    return render(request, 'users/Ivanov.html')

def list_of_students(request):
    return render(request, 'users/list_of_students.html')

def list_of_teachers_for_groups(request):
    return render(request, 'users/list_of_teachers_for_groups.html')

def List_of_teachers(request):
    return render(request, 'users/List_of_teachers.html')

def Massages(request):
    return render(request, 'users/Massages.html')

def Pilipenko(request):
    return render(request, 'users/Pilipenko.html')

def profile_admin(request):
    return render(request, 'users/profile_admin.html')

def registed_users(request):
    return render(request, 'users/registed_users.html')