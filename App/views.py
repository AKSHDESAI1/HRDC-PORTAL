from traceback import print_tb
from django.forms import ValidationError
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.


def home(request):
    return render(request, 'App/Home.html')


def login1(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        result = authenticate(username=username, password=password)
        if result is not None:
            login(request, result)
            return redirect('home1')
        else:
            messages.error(request, 'Username or Password is incorrect')
    form = AuthenticationForm()
    context = {'form': form}
    return render(request, 'App/login.html', context)


def home1(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return render(request, 'App/admin_dashboard.html')
        else:
            return render(request, 'App/user_dashboard.html')
    else:
        return redirect('login')

def logout1(request):
    logout(request)
    return redirect('login')