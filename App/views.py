from .models import Event
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import datetime

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


def announcement(request):
    return render(request, 'App/announcement.html')


def list_announcement(request):
    data = Event.objects.all()
    context = {'data': data}
    print(data)
    return render(request, 'App/list_announcement.html', context)


def add_announcement(request):
    if request.method == 'POST':
        academicyear = request.POST['academmicyear']
        eventname = request.POST['eventname']
        eventfocus = request.POST['eventfocus']
        eventstartdate = request.POST['eventstartdate']
        eventenddate = request.POST['eventenddate']
        eventvenue = request.POST['eventvenue']
        eventresourceperson = request.POST['eventresourceperson']
        starttime = []
        endtime = []
        for i in range(1, (int(eventenddate[8:]) - int(eventstartdate[8:]) + 1) + 1):
            starttime.append(request.POST[f'starttime{i} '])
            endtime.append(request.POST[f'endtime{i} '])
        doc = Event(academicyear=academicyear, eventname=eventname, eventfocus=eventfocus, eventstartdate=eventstartdate,
                    eventenddate=eventenddate, eventvenue=eventvenue, eventresourceperson=eventresourceperson, starttime=starttime, endtime=endtime)
        doc.save()
        # print(starttime)
        # print(endtime)
        # print(eventstartdate[8:])
        # print(eventenddate[8:])
        # print(int(eventenddate[8:]) - int(eventstartdate[8:]) + 1)
        # print('starttime1', request.POST['starttime1 '])
        # print(f"academmicyear {academmicyear}")
        # print(f"eventname {eventname}")
        # print(f"eventfocus {eventfocus}")
        # print(f"eventstartdate {eventstartdate}")
        # print(f"eventenddate {eventenddate}")
        # print(f"eventvenue {eventvenue}")
        # print(f"eventresourceperson {eventresourceperson}")

        return HttpResponse('<h1> meow </h1>')
    return render(request, 'App/add_announcement.html')
