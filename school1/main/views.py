from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import context

from django.views.generic import DetailView

from main.models import Categories
from main.models import Subjects
from main.models import Teachers
from main.models import About_us

def index(request):
    categories = Categories.objects.all()
    return render(request, 'main/index.html', {"categories": categories})


def About_us (request):
    return render(request, 'main/About_us.html' )

def Contacts_of_teachers (request):
    return render(request, 'main/Contacts_of_teachers.html' )



def My_students (request):
    return render(request, 'main/My_students.html' )

def Plan (request):
    return render(request, 'main/Plan.html' )

def Students (request):
    return render(request, 'main/Students.html' )

def Teachers (request):
    return render(request, 'main/Teachers.html')

def subjects_all (request, subjects_slug):
    subject=Subjects.objects.get(slug=subjects_slug)
    context={
        'subject': subject
    }
    return render(request, 'main/subjects_all.html', context=context)
