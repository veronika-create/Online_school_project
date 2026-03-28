from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404

#from main.models import Categories
from main.models import Subjects
#from main.models import Teachers
#from main.models import About_us

def index (request):
    
    return render(request, 'main/index.html')

def About_us (request, about_us_slug):
    about_us= get_object_or_404 (About_us, slug=about_us_slug)
    return render(request, 'main/About_us.html', {'about_us': about_us})

def Log_in (request, subjects_slug):
    subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    return render(request, 'main/Log_in.html', {'subjects':  subjects})

#def Subjects_all (request, subjects_slug):
    #subjects= get_object_or_404 (Subjects, slug=subjects_slug)

    #return render(request, 'main/Subjects_all.html', {'subjects':  subjects})

#def connect(request):
    #return render(request, 'main/connect.html')

#def main(request):
    #return render(request, 'main/main.html')

def Analytic(request, subjects_slug):
    subjects= get_object_or_404 (Subjects, slug=subjects_slug)

    return render(request, 'main/Analytic.html', {'subjects':  subjects})    

def Design(request, subjects_slug):
    subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    return render(request, 'main/Design.html', {'subjects':  subjects})

def Finance(request, subjects_slug):
    subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    return render(request, 'main/Finance.html', {'subjects':  subjects})

def Managing (request, subjects_slug):
    subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    return render(request, 'main/Managing.html', {'subjects':  subjects})

def Marketing (request, subjects_slug):
    subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    return render(request, 'main/Marketing.html', {'subjects':  subjects})

def Programming (request, subjects_slug):
    subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    return render(request, 'main/Programming.html', {'subjects':  subjects})
    

def Teachers (request, teacher_slug):
    teacher= get_object_or_404 (Teachers, slug=teacher_slug)
    return render(request, 'main/Teachers.html', {'teacher':  teacher})