from django import forms
from testing.models import Test, Question, Answer, Choice

class testing(forms.ModelForm):

    class Meta:
        model = Test
        fields = ['question', 'option1', 'option2', 'option3', 'option4']


question = forms.CharField()
option1 = forms.CharField()
option2 = forms.CharField()
option3 = forms.CharField()
option4 = forms.CharField()

 
class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = (
            'name',
            'qtype',
            'explanation'
        )

name = forms.CharField()
qtype = forms.CharField()
explanation = forms.CharField()

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = (
            'question',
            'name',
            'is_correct'
        )


question = forms.CharField()
name = forms.CharField()
is_correct = forms.BooleanField()

class ChoiceForm(forms.ModelForm):
    class Meta:
        model = Choice
        fields = (
            'question',
            'answer',
        )

question = forms.CharField()
answer = forms.CharField()