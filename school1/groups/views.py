from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.template import context

from django.views.generic import DetailView

from groups.models import Courses, Groups, Teachers_сourses, Teachrs_groups





def courses_list (request):
    courses= Courses.objects.all()
    return render(request, 'groups/Courses.html', {"courses":courses} )

def groups_list(request):
    groups = Groups.objects.all()        
    return render(request, "groups/Groups.html", {"groups": groups})

def My_courses_list (request):
    mycourses=Teachers_сourses.objects.all()
    return render(request, 'groups/My_courses.html', {"mycourses": mycourses} )

def My_groups_list (request):
    mygroups = Teachrs_groups.objects.all()
    return render(request, 'groups/My_groups.html', {"mygroups":mygroups} )

