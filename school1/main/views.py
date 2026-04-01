from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import ListView

from main.models import Categories
from main.models import Subjects
from main.models import Teachers
from main.models import About_us

def index(request):
    categories = Categories.objects.all()
   
    return render(request, 'main/index.html', {"categories": categories})

def About_us (request):
    return render(request, 'main/About_us.html')

def Subjects_all (request, subjects_slug):
    subjects = Subjects.objects.get(slug=subjects_slug)
   
    context={
    "subjects": subjects,
    #"category_selected": subjects.category_slug,
    }
    return render(request, 'main/Subjects_all.html', context = context, )
    #subjects = Subjects.objects.get(slug=subjects_slug)


    #categories = get_object_or_404 (Subjects, slug=subjects_slug)
    #return render(request, 'main/Subjects_all.html', {"categories": categories} )
    #categories = Subjects.objects.get(slug=subjects_slug)
#categories = Categories.objects.all
    #categories= get_object_or_404 (Subjects, slug=slug)
    #slug= "None"
    #return render(request, 'main/Subjects_all.html', {"categories": categories})
    #,
def Log_in(request):
    return render(request, 'main/Log_in.html')

def Teachers (request):
    return render(request, 'main/Teachers.html')

#def Categories (request, categories_slug):
    #categories= get_object_or_404 (Categories, slug=category_slug)

    #return render(request, 'main/index.html.html', {'categories': category})

#def connect(request):
    #return render(request, 'main/connect.html')

#def main(request):
    #return render(request, 'main/main.html')

#def Analytic(request, categories_slug):
    #categories= get_object_or_404 (Subjects, slug=categories_slug)

    #return render(request, 'main/Analytic.html', {'categories': category})    

#def Design(request, subjects_slug):
    #subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    #return render(request, 'main/Design.html', {'subjects':  subjects})

#def Finance(request, subjects_slug):
    #subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    ##return render(request, 'main/Finance.html', {'subjects':  subjects})

#def Managing (request, subjects_slug):
    #subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    #return render(request, 'main/Managing.html', {'subjects':  subjects})

#def Marketing (request, subjects_slug):
    #subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    #return render(request, 'main/Marketing.html', {'subjects':  subjects})

#def Programming (request, subjects_slug):
    #subjects= get_object_or_404 (Subjects, slug=subjects_slug)
    #return render(request, 'main/Programming.html', {'subjects':  subjects})
    

