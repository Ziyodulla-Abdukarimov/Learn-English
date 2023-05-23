from django.shortcuts import render
from .models import UZVerb, Choice


# Create your views here.
def list_quizzes(request):
    verb = UZVerb.objects.order_by('?')[:1]
    context = {
        'quizzes': verb,
        'choices': Choice.objects.filter(question=verb)
    }
    return render(request, 'list-quizzes.html', context)
