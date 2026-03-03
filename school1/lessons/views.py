from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'lessons/index.html')

def about_us_std(request):
    return render(request, 'lessons/about_us_std.html')
