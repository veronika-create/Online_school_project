from django import template

from lessons.models import Lessons



register = template.Library()

@register.simple_tag()
def tag_lessons ():
    return  Lessons.objects.all() 