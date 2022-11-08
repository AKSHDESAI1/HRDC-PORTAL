from urllib import response
from .models import Event
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import datetime
from .models import Nomination
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
    if request.user.is_superuser == True:
        data = Event.objects.all()
        context = {'data': data, 'super': True}
        return render(request, 'App/list_announcement.html', context)
    else:
        data = Event.objects.all()
        context = {'data': data, 'super': False}
        return render(request, 'App/list_announcement.html', context)


def add_announcement(request):
    if request.method == 'POST':
        print("rudra", request.POST)
        academicyear = request.POST['academicyear']
        eventname = request.POST['eventname']
        eventfocus = request.POST['eventfocus']
        eventstartdate = request.POST['eventstartdate']
        eventenddate = request.POST['eventenddate']
        eventvenue = request.POST['eventvenue']
        eventresourceperson = request.POST['eventresourceperson']
        starttime = []
        endtime = []

        for i in range(1, (int(eventenddate[8:]) - int(eventstartdate[8:]) + 2)):
            print(f'starttime{i}', request.POST[f'starttime{i}'])
            print(f'endtime{i}', request.POST[f'endtime{i}'])
            starttime.append(request.POST[f'starttime{i}'])
            endtime.append(request.POST[f'endtime{i}'])

        print("starttime", starttime)
        print("endtime", endtime)

        doc = Event(academicyear=academicyear, eventname=eventname, eventfocus=eventfocus, eventstartdate=eventstartdate,
                    eventenddate=eventenddate, eventvenue=eventvenue, eventresourceperson=eventresourceperson, starttime=starttime, endtime=endtime)
        doc.save()

        # print(starttime)
        # print(endtime)
        # print(eventstartdate[8:])
        # print(eventenddate[8:])
        # print(int(eventenddate[8:]) - int(eventstartdate[8:]) + 1)
        # print('starttime1', request.POST['starttime1 '])

        # print(f"academmicyear {academicyear}")
        # print(f"eventname {eventname}")
        # print(f"eventfocus {eventfocus}")
        # print(f"eventstartdate {eventstartdate}")
        # print(f"eventenddate {eventenddate}")
        # print(f"eventvenue {eventvenue}")
        # print(f"eventresourceperson {eventresourceperson}")
        return HttpResponseRedirect('/list_announcement')
    return render(request, 'App/add_announcement.html')


def edit_announcement(request, myid):
    id = Event.objects.filter(id=myid)
    return render(request, 'App/edit_announcement.html')


def nomination(request):
    if request.user.is_superuser:
        a1 = Nomination.objects.all()
        return render(request, 'App/admin_nomination.html', {'a1': a1})
    else:
        if request.method == "POST":
            EmployeeName = request.POST['name']
            EmployeeId = request.POST['id']
            Branch = request.POST['branch']
            FunctionDepartment = request.POST['fDepa']
            ContactNo = request.POST['phone']
            ContactNoMobile = request.POST['phone1']
            ReportingAuthority = request.POST['authority']
            TotalExperience = request.POST['experience']
            TotalExperienceField = request.POST['expField']
            TotalTeachingExperience = request.POST['teaExp']
            TotalTeachingExperienceField = request.POST['teaExpfield']
            Batch = request.POST['batch']

            data = Nomination(EmployeeName=EmployeeName,
                              EmployeeId=EmployeeId,
                              Branch=Branch,
                              FunctionDepartment=FunctionDepartment,
                              ContactNo=ContactNo,
                              ContactNoMobile=ContactNoMobile,
                              ReportingAuthority=ReportingAuthority,
                              TotalExperience=f'{TotalExperience} - {TotalExperienceField}',
                              TotalTeachingExperience=f'{TotalTeachingExperience} - {TotalTeachingExperienceField}',
                              Batch=Batch)
            data.save()
            messages.success(
                request, 'Nomination has been Succeffully Registered.')
        return render(request, "App/nomination.html")


def nomination1(request):
    return render(request, "App/1nomination.html")


def batchwise_nomination(request):
    return render(request, "App/batchwise_nomination.html")


def download_nomi_admin(request):
    return render(request, "App/download_nomi_admin.html")


def download_excel(request):
    a1 = Nomination.objects.all()
    return render(request, "App/admin_nomination.html", {'a1': a1})
