from django.shortcuts import render, get_object_or_404, redirect
from .models import UZVerb, Choice


# Create your views here.
def list_quizzes(request):
    verb = UZVerb.objects.order_by('?')[:1]
    if request.method == 'POST':
        button = request.POST['button']
        if get_object_or_404(Choice, id=button).is_correct:
            return redirect('correct')
        else:
            return redirect('wrong')
    context = {
        'quizzes': verb,
        'choices': Choice.objects.filter(question=verb)
    }
    return render(request, 'list-quizzes.html', context)


def correct(request):
    return render(request, 'correct.html')


def wrong(request):
    return render(request, 'wrong.html')
