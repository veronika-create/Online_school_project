from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from lessons.models import Lessons

def index(request):
    lessons = Lessons.objects.all()
    return render(request, 'lessons/index.html', {"lessons": lessons})

def about_us_std(request):
    return render(request, 'lessons/about_us_std.html')

def lessons_all (request, lessons_slug):
    lesson=Lessons.objects.get(slug=lessons_slug)
    context={
        'lesson': lesson
    }
    return render(request, 'lessons/lessons_all.html', context=context)
#class LessonsDetailView (DetailView):
    #model=Lessons
    #template_name='lessons/lessons_all.html'
    #slug_url_kwarg= 'lessons_slug'
    #context_object_name = 'lessons'
    #slug_field = 'slug'

    #def get_context_data(self, **kwargs):
        #context = super().get_context_data(**kwargs)
        
        #return context
    

    #def get_object (self, queryset=None):
        #return get_object_or_404 (Lessons, slug=self.kwargs[self.slug_url_kwarg])
    
def Log_in(request):
    return render(request, 'lessons/Log_in.html')

def Profile_std(request):
    return render(request, 'lessons/Profile_std.html')