from django import forms
from testing.models import Test


class testing(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['question', 'option1', 'option2', 'option3', 'option4']


question = forms.CharField()
option1 = forms.CharField()
option2 = forms.CharField()
option3 = forms.CharField()
option4 = forms.CharField()
