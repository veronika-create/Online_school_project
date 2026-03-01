from django.http import HttpResponse
from django.shortcuts import render



def list_of_students(request):
    return render(request, 'orders/list_of_students.html')

def list_of_teachers_for_groups(request):
    return render(request, 'orders/list_of_teachers_for_groups.html')

def list_of_teachers(request):
    return render(request, 'orders/list_of_teachers.html')

def Massages(request):
    return render(request, 'orders/Massages.html')

def results(request):
    return render(request, 'orders/results.html')