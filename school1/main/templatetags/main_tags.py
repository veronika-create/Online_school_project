from django import template

from main.models import Categories
from main.models import Subjects
from main.models import Teachers
from main.models import About_us


register = template.Library()

@register.simple_tag()
def tag_categories ():
    return  Categories.objects.all() 

@register.simple_tag()
def tag_subjects ():
    return  Subjects().objects.all() 

@register.simple_tag()
def tag_teachers ():
    return  Teachers().objects.all() 

@register.simple_tag()
def tag_About_us ():
    return  About_us().objects.all() 