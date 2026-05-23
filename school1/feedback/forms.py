from django import forms
from feedback.models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = (
            'name',
            'email',
            'description'
        )

name = forms.CharField()
email = forms.CharField()
description = forms.CharField()

 
