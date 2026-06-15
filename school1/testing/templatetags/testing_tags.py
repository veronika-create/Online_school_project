from django import template

from testing.models import Test



register = template.Library()

@register.simple_tag()
def tag_testing ():
    return  Test.objects.all() 

