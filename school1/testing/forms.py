from django import forms
from testing.models import Test


class TestAddForm(forms.ModelForm):

    choice1 = forms.CharField(label='Choice 1', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice2 = forms.CharField(label='Choice 2', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice3 = forms.CharField(label='Choice 3', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))
    choice4 = forms.CharField(label='Choice 4', max_length=100, min_length=1,
                              widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Test
        fields = ['text', 'choice1', 'choice2', 'choice3', 'choice4']
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }


class EditTestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'cols': 20}),
        }

