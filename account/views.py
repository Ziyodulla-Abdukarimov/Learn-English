from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as log_out
from .models import User
from django.contrib import messages


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(username=username, password=password1)
                user = authenticate(request, username=username, password=password1)
                if user is not None:
                    login_user(request, user)
                    return redirect('main')
            else:
                messages.error(request, "Bunday foydalanuvhi mavjud!")
                return redirect('register')
            return redirect('dashboard')
        else:
            messages.error(request, "Parol bir xil emas!")
            return redirect('register')
    return render(request, 'account/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('main')

    return render(request, 'account/login.html')


def logout(request):
    log_out(request)
    return redirect('dashboard')