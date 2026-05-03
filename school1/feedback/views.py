from django.core.mail import EmailMultiAlternatives
from django.forms.renderers import get_template
from django.shortcuts import render, redirect
from feedback.models import Feedback
from django.views.generic import View

class FeedbackView(View):
  
    def post (self, request):
        #context = ()
        if request.mothod == 'POST':
            form = FeedbackView (data=request.POST)
            if form.is_valid():
                    form.save()
                #send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['description'])
            context= {
            'form': form,
          }
            return render(request, 'messages.html, context=context')
        else:
            form= FeedbackView()
        context= {
        'form': form,
          }
        return render(request, 'message.html, context=context')
     
def send_message (name, email, description):
    text = get_template('messages.html')
    html = get_template('messages.html')
    context = {'name': name, 'email': email, 'description': description}
    subject = 'Обращение от пользователя'
    form_email= 'form@example.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msq = EmailMultiAlternatives(subject, text_content, form_email, ['form@example.com'])
    msq.attach_alternative(html_content, 'text/html')
    msq.send()