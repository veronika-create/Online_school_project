from django.http.response import HttpResponseRedirect

from feedback.forms import FeedbackForm
from django.core.mail import EmailMultiAlternatives
from django.forms.renderers import get_template
from django.shortcuts import render, redirect
from django.urls import reverse
from feedback.models import Feedback



def feedback(request):
    if request.method == 'POST':
        form = FeedbackForm (data=request.POST)
        if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('main:index'))
    else:
        form= FeedbackForm()

    context= {
        'title': 'Home - Обратная связь',
        'form': form,
          }
    return render(request, 'feedback/messages.html', context=context)


def questions (request):
    feedback  = Feedback.objects.all()
    return render(request, 'feedback/feedback.html', {"feedback": feedback})