
from testing.forms import QuestionForm, AnswerForm, ChoiceForm 
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from testing.models import Result, Test, Question, Result, Choice, Answer

from django.db.models import F

#@login_required
#def tests(request):
	#questions =  Question.objects.all()

	#return render(request, 'testing/test.html', { 'questions': questions})

@login_required
def tests(request):
    if request.method == 'POST':
        form = ChoiceForm (data=request.POST)
        question = Choice.objects.all()
        if question.qtype == 'single':
            correct_answer = question.get_answers()
            choice = Choice(user=request.user, 
                form=form)
            choice.save()
            is_correct = correct_answer
            result, created = Result.objects.get_or_create(user=request.user)
            if is_correct is True:
                result.correct = F('correct') + 1
            else:
                result.wrong = F('wrong') + 1
            result.save()

        elif question.qtype == 'multiple':
            correct_answer = question.get_answers()
            answers_ids = request.POST.getlist('answer')
            if answers_ids:
                for answer_id in answers_ids:
                    choice = Choice(user=request.user, 
                        question=question, )
                    choice.save()
                is_correct = correct_answer
                result, created = Result.objects.get_or_create(user=request.user)
                if is_correct is True:
                    result.correct = F('correct') + 1
                else:
                    result.wrong = F('wrong') + 1
                result.save()

    return render (request, 'testing/test.html')

@login_required
def test_results(request):
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