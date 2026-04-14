from django import forms
from feedback.models import Feedback

class Feedbackform(form.Modelform):
    
    class Meta:
        model = Feedback
        fielsd = ['name', 'email', 'description']
