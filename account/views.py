from django.shortcuts import render
from .models import User
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['confirm-password']
        if password1 == password2:
            User.objects.create_user(username=username, email=email, password=password1)
        else:
            messages.error(request, "Kiritilgan parol bir xil emas!")

    return render(request, 'account/register.html')


def login(request):
    return render(request, 'account/login.html')
