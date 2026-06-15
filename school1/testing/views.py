from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from testing.forms import  testing
from testing.models import Result, Test, Question, Result, Choice, Answer

from django.db.models import F

def tests(request):
	questions = Test.objects.all()

	return render(request, 'testing/test.html', { 'questions': questions})

@login_required
#def test(request):
    #if question.qtype == 'single':
           # correct_answer = question.get_answers()
           # user_answer = question.answer_set.get(pk=request.POST['answer'])
            #choice = Choice(user=request.user, 
                #question=question, answer=user_answer)
            #choice.save()
            #is_correct = correct_answer == user_answer
           # result, created = Result.objects.get_or_create(user=request.user)
           # if is_correct is True:
               # result.correct = F('correct') + 1
           # else:
                #result.wrong = F('wrong') + 1
           # result.save()

       
        
#return render (request, 'testing/test.html')

@login_required
def test_results(request, test_id):
    questions = test.question_set.all()
    results = Result.objects.filter(user=request.user).values()
    correct = [i['correct'] for i in results][0]
    wrong = [i['wrong'] for i in results][0]
    context = {
    'correct': correct, 
    'wrong': wrong, 
    'number': len(questions), 
    'skipped': len(questions) - (correct + wrong)}
    return render(request, 
        'testing/results.html', context)