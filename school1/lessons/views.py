from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from import_export import resources
from lessons.models import Lessons
from lessons.resource import LessonsResource


def lessons(request):
    lessons = Lessons.objects.all()
    return render(request, 'lessons/lessons.html', {"lessons": lessons})

def lessons_all (request, lessons_slug):
    lesson=Lessons.objects.get(slug=lessons_slug)
   
    context={
        'lesson': lesson
        }
    return render(request, 'lessons/lessons_all.html', context=context)