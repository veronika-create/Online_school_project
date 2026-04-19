from django.contrib import messages

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from testing.forms import EditTestForm, TestAddForm
from testing.models import Test

def tests(request):
	questions = Test.objects.all()

	return render(request, 'testing/test.html', { 'questions': questions})


def test_add(request):
    if request.user.has_perm('test.test_add'):
        if request.method == 'POST':
            form = TestAddForm(request.POST)
            if form.is_valid:
                test = form.save(commit=False)
                test.owner = request.user
                test.save()
                Choice(
                    test=test, choice_text=form.cleaned_data['choice1']).save()
                Choice(
                    test=test, choice_text=form.cleaned_data['choice2']).save()

                messages.success(
                    request, "Изменения успешно тобавлены.", extra_tags='alert alert-success alert-dismissible fade show')

                return redirect('testing/test.html')
        else:
            form = TestAddForm()
        context = {
            'form': form,
        }
        return render(request, 'testing/test_add.html', context)
    else:
        return HttpResponse("Извините, но у вас нет на это разрешения!")



def test_edit(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    if request.user != test.owner:
        return redirect('main:index')

    if request.method == 'POST':
        form = EditTestForm(request.POST, instance=test)
        if form.is_valid:
            form.save()
            messages.success(request, "Теуст успешно изменён.",
                             extra_tags='alert alert-success alert-dismissible fade show')
            return redirect("testing:test")

    else:
        form = EditTestForm(instance=test)

    return render(request, "testing/test_edit.html", {'form': form, 'test': test})



def test_delete(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    if request.user != test.owner:
        return redirect('main:index')
    test.delete()
    messages.success(request, "Тест удалён.",
                     extra_tags='alert alert-success alert-dismissible fade show')
    return redirect("users:profile")


def end_test(request, test_id):
    test = get_object_or_404(Test, pk=test_id)
    if request.user != test.owner:
        return redirect('testing:results')

    if test.active is True:
        test.active = False
        test.save()
        return render(request, 'testing/results.html', {'test': test})
    else:
        return render(request, 'testing/results.html', {'test': test})

