from django import forms
from testing.models import Test


class TestingForm(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['question', 'choice1', 'choice2', 'choice3', 'choice4']




