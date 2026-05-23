from feedback.forms import FeedbackForm
from django.core.mail import EmailMultiAlternatives
from django.forms.renderers import get_template
from django.shortcuts import render, redirect
from feedback.models import Feedback



def feedback(request):
    if request.method == 'POST':
            form = FeedbackForm (data=request.POST)
            if form.is_valid():
                form.save()
         
            return redirect(request, 'feedback/messages.html', {'form': form})


def questions (request):
    feedback  = Feedback.objects.all()
    return render(request, 'feedback/feedback.html', {"feedback": feedback})