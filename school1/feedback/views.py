
from django.shortcuts import render, redirect
from feedback.forms import FeedbackForm
from feedback.models import Feedback
from django.http.response import HttpResponseRedirect

def Messages (request):
    
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(redirect('feedback:feedback'))
    else:
        form = FeedbackForm()
    context= {
        'form': form,
          }
    return render(request, 'feedback/messages.html', context=context)  

def feedback (request):
    feedback  = Feedback.objects.all()
    return render(request, 'feedback/feedback.html', {"feedback": feedback})