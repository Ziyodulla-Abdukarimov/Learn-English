from django.shortcuts import render
from model.models import Course


# Create your views here.
def home(request):
    return render(request, 'index.html')


def courses(request):
    context = {
        'courses': Course.objects.all(),
    }
    return render(request, 'courses.html', context)


def course_detail(request, pk):
    context = {
        'course_detail': Course.objects.get(id=pk),
    }
    return render(request, 'course-detail.html', context)


def about(request):
    return render(request, 'about.html')
