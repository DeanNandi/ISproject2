from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Student, Search
from .forms import MyForm, SearchCourse
from .models import Registration
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from lecturer.models import Ams
from lecturer.models import Unitregister

def registerStudent(request):
    if request.user.is_authenticated:
        return redirect('student-home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login-student/')

        context = {'form': form}
        return render(request, 'register-student.html', context)


def loginStudent(request):
    if request.user.is_authenticated:
        return redirect('student-home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('student-home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login-student.html', context)


def logoutStudent(request):
    logout(request)
    return redirect('login-student/')

def my_form(request):

  if request.method == "POST":
    form = MyForm(request.POST)
    if form.is_valid():
      form.save()
  else:
      form = MyForm()
  return render(request, 'registration.html', {'form': form})


def studenthome(request):
    student = Student.objects.all()
    return render(request, 'studenthome.html', {'student': student })


def getqr(request):
    ams = Ams.objects.all()
    return render(request, 'getqr.html', {'ams':ams})

def getatt(request):
    unitregister = Unitregister.objects.all()
    return render(request, 'getatt.html', {'unitregister': unitregister})

def report_student(request):
    if request.method == "POST":
        form = SearchCourse(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SearchCourse()
    return render(request, 'getqr.html', {'form': form})



def student(request):
    return render(request, 'student.html', {})
