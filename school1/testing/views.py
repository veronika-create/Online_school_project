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
