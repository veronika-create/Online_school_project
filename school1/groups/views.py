from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'groups/index.html')

def about_us_prep(request):
    return render(request, 'groups/about_us_prep.html')

def base_of_knowledge(request):
    return render(request, 'groups/base_of_knowledge.html')

def Courses(request):
    return render(request, 'groups/Courses.html')

def Groups(request):
    return render(request, 'groups/groups.html')

def Help_prep(request):
    return render(request, 'groups/Help_prep.html')

def Lectures(request):
    return render(request, 'groups/Lectures.html')

def material_for_students(request):
    return render(request, 'groups/material_for_students.html')

def profile_prep(request):
    return render(request, 'groups/profile_prep.html')

def results(request):
    return render(request, 'groups/results.html')

def Tests(request):
    return render(request, 'groups/Tests.html')