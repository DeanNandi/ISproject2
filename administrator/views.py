from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Timetable
from .forms import NewsletterForm
from .models import Email
from django.contrib import messages
from django.core.mail import EmailMessage
from .models import BBIT
from .forms import BbitForm
from .models import BTC
from .forms import BtcForm
from .models import ICS
from .forms import IcsForm
from django.contrib.auth.forms import UserCreationForm
# from .forms import UserRegistrationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('admininfo')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login-admin/')

        context = {'form': form}
        return render(request, 'registers.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('admininfo')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('admininfo')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login-page.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login-admin/')



def bbit_register(request):
    if request.method == "POST":
        form = BbitForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BbitForm()
    return render(request, 'BbitRegister.html', {'form': form})

def btc_register(request):
    if request.method == "POST":
        form = BtcForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BtcForm()
    return render(request, 'BtcRegistration.html', {'form': form})

def ics_register(request):
    if request.method == "POST":
        form = IcsForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = IcsForm()
    return render(request, 'IcsRegistration.html', {'form': form})

class DepartmentReports(View):
        def class_bbit(request):
            bbit = BBIT.objects.all()
            return render(request, 'LecReports.html', {'bbit': bbit})

        def class_btc(request):
            btc = BTC.objects.all()
            return render(request, 'btc-reports.html', {'btc': btc})

        def class_ics(request):
            ics = ICS.objects.all()
            return render(request, 'ics-reports.html', {'ics': ics})


def class_assign(request):
    return render(request, 'lecclass.html', {})


def lecturer_page(request):
    return render(request, 'lecturerpage.html', {})


def admin_info(request):
    return render(request, 'admininfo.html', {})

def main_page(request):
    return render(request, 'mainpage.html', {})

def bbit_reports(request):
    bbit = BBIT.objects.all()
    return render(request, 'bbitreports.html', {'bbit':bbit})


def btc_reports(request):
    btc = BTC.objects.all()
    return render(request, 'btcreports.html', {'btc':btc})

def ics_reports(request):
    ics = ICS.objects.all()
    return render(request, 'icsreports.html', {'ics':ics})

def admin(request):
    return render(request, 'administrator.html', {})

def newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get('subject')
            receivers = form.cleaned_data.get('receivers').split(',')
            email_message = form.cleaned_data.get('message')

            mail = EmailMessage(subject, email_message, f"Dean Nandi <dean.nandi@strathmore.edu>", bcc=receivers)
            mail.content_subtype = 'html'

            if mail.send():
                messages.success(request, "Email sent succesfully")
            else:
                messages.error(request, "There was an error sending email")

        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

        return redirect('/')
    form = NewsletterForm()
    return render(request, 'newsletter.html', {'form': form})


def courses_two(request):
    return render(request, 'courses.html', {})

def depart(request):
    return render(request, 'departments.html', {})

def landing(request):
    return render(request, 'landing.html', {})


def timetable(request):
    if request.method == 'POST':
        monday = request.POST['monday']
        tuesday = request.POST['tuesday']
        wednesday = request.POST['wednesday']
        thursday = request.POST['thursday']
        friday = request.POST['friday']

        timetable = Timetable.objects.create(monday, tuesday, wednesday, thursday, friday)

    return render(request, 'EditTimetable.html' )





