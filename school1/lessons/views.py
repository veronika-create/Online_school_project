from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from import_export import resources
from lessons.models import Lessons, Marks, Teachers_paln, homework, stud_marks, table, Library
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

def Marks_list (request):
    marks = Marks.objects.all()

    return render(request, 'lessons/Marks.html', {"marks":marks})

def Plan_list (request):
    plans = Teachers_paln.objects.all()
    return render(request, 'lessons/Plan.html', {"plans":plans})

def homework_list  (request):
    ws=homework.objects.all()
    return render(request, 'lessons/homework.html',  { "ws":ws} )

def stud_marks_list  (request):
    sms=stud_marks.objects.all()
    return render(request, 'lessons/Ivanov_marks.html',  { "sms":sms})

def table_list  (request):
    tbs=table.objects.all()
    return render(request, 'lessons/table.html',  { "tbs":tbs} )

def Library_list  (request):
    libs=Library.objects.all()
    return render(request, 'lessons/library.html',  { "libs":libs} )
