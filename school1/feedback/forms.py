from django import forms
from feedback.models import Feedback

class Feedbackform(forms.Form):
    name = forms.CharField(
        min_length=2,
        wideget=forms.TextInput()

    )

    email = forms.EmailField(
        wideget=forms.EmailInput()

    )

    message = forms.CharField(
        min_length=20,
        wideget=forms.Textarea()
    )

    class Meta:
        model = Feedback
        fielsd = ['name', 'email', 'description']
