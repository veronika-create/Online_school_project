from django import template

from feedback.models import Feedback



register = template.Library()

@register.simple_tag()
def tag_feedback ():
    return  Feedback.objects.all() 