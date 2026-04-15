from django.shortcuts import render

from testing.models import Test

def tests(request):
	questions = Test.objects.all()

	return render(request, 'tests.html', { 'questions': questions})


