from django import template

from groups.models import Courses, Groups, Teachers_сourses, Teachrs_groups


register = template.Library()

@register.simple_tag()
def tag_courses ():
    return  Courses.objects.all() 

@register.simple_tag()
def tag_groups ():
    return  Groups.objects.all() 

@register.simple_tag()
def tag_teachers_сourses ():
    return  Teachers_сourses.objects.all() 

@register.simple_tag()
def tag_teachrs_groups():
    return  Teachrs_groups.objects.all() 