
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from testing.forms import TestingForm

from testing.models import Test

@login_required
def tests(request):
	questions = Test.objects.all()
	
	if request.method == "POST":
		form=TestingForm (data=request.POST)
		selected_option = request.POST['questions']
		if selected_option == 'option1':
			questions.option1_count += 1
			form.save()

		elif selected_option == 'option2':
			questions.option2_count += 0
			form.save()

		elif selected_option == 'option3':
			questions.option3_count += 0
			form.save()

		elif selected_option == 'option4':
			questions.option4_count += 0
			form.save()

		else:
			form=TestingForm()

			return HttpResponseRedirect(reverse('main:index'))
		
		form.save()

	context= {
        'form': form,
          }


	return render(request, 'testing/test.html', context=context)

@login_required
def results(request):
	answers = Test.objects.all()

	return render(request, 'testing/results.html', { 'answers': answers})
