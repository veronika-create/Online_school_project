from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'lessons/index.html')

def about_us_std(request):
    return render(request, 'lessons/about_us_std.html')

def Cookie(request):
    return render(request, 'lessons/Cookie.html')

def History(request):
    return render(request, 'lessons/History.html')

def Massyvy(request):
    return render(request, 'lessons/Massyvy.html')

def Methods(request):
    return render(request, 'lessons/Methods.html')

def MySQL_in_PHP(request):
    return render(request, 'lessons/MySQL_in_PHP.html')

def Obgects(request):
    return render(request, 'lessons/Obgects.html')

def Profile_std(request):
    return render(request, 'lessons/Profile_std.html')

def Syntacsis(request):
    return render(request, 'lessons/Syntacsis.html')
