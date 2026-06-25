from django.http.response import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from testing.models import TestQuestion, UserAnswer, TestChoice
from django.db.models import Count, Q

def test(request):
    questions = TestQuestion.objects.prefetch_related('choices').all()
    if request.method == 'POST':
        for q in questions:
            choice_id = request.POST.get(f'choice_{q.id}')
            if choice_id:
                choice = get_object_or_404(TestChoice, id=choice_id, question=q)
                UserAnswer.objects.update_or_create(
                    user=request.user if request.user.is_authenticated else None,
                    question=q,
                    defaults={'selected_choice': choice}
                )
        return HttpResponseRedirect (reverse('testing:results'))
    
    return render(request, 'testing/test.html', {'questions': questions})

def results(request):
    qs = UserAnswer.objects.select_related('question', 'selected_choice')
    if not request.user.is_authenticated:
        # для анонимных можно фильтровать по сессии или вообще не показывать личные результаты
        qs = qs.none()
    else:
        qs = qs.filter(user=request.user)

    total = qs.count()
    correct = qs.filter(selected_choice__is_correct=True).count()
    percentage = (correct / total * 100) if total else 0

    answers = qs.order_by('question__id')

    return render(request, 'testing/results.html', {
        'answers': answers,
        'total': total,
        'correct': correct,
        'percentage': percentage,
    })