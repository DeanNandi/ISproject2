from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Lecturer
from django.contrib.auth import get_user_model, login
from .form import UserRegistrationForm
from django.contrib import messages
from .form import LecRegister
from .models import Qrcode
from .form import QrRegister, PostForm
from .models import Post
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.generic.base import View
from .form import UploadForm, AmsRegister
from csv import DictReader
from io import TextIOWrapper
from .models import Ams
from .form import UploadRegister, UnitRegister


class UploadViews(View):
    def get(self, request, *args, **kwargs):
        return render(request, "registeredupload.html", {"form": UploadRegister()})

    def post(self, request, *args, **kwargs):
        register_file = request.FILES["register_file"]
        rows = TextIOWrapper(register_file, encoding="utf-8", newline="")
        for row in DictReader(rows):
            form = UnitRegister(row)
            form.save()
        return render(request, "registeredupload.html", {"form": UploadForm()})


class UploadView(View):

    def get(self, request, *args, **kwargs):
        return render(request, "upload.html", {"form": UploadForm()})

    def post(self, request, *args, **kwargs):
        attendance_file = request.FILES["attendance_file"]
        rows = TextIOWrapper(attendance_file, encoding="utf-8", newline="")
        for row in DictReader(rows):
            form = AmsRegister(row)
            form.save()
        return render(request, "upload.html", {"form": UploadForm()})

@login_required(login_url="login")
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("delete_post")):
                post.delete()
        elif user_id:
            user = User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.get(name='default')
                    group.user_set.remove(user)
                except:
                    pass

                try:
                    group = Group.objects.get(name='mod')
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'home.html', {"posts": posts})


@login_required(login_url="login")
@permission_required("main.add_post", login_url="login", raise_exception=True)
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("home")
    else:
        form = PostForm()

    return render(request, 'create_post.html', {"form": form})

def lec_register(request):
    if request.method == "POST":
        form = LecRegister(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LecRegister()
    return render(request, 'LecRegister.html', {'form': form})


def register(request):
    # Logged in user can't register a new account
    if request.user.is_authenticated:
        return redirect("index.html")

    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"New account created: {user.username}")
            return redirect('index.html')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)

    else:
        form = UserRegistrationForm()

    return render(
        request = request,
        template_name = "register.html",
        context={"form":form}
        )


def index2(request):
    return render(request, 'index2.html', {})


def index(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'index.html', {'lecturer': lecturer })


def details(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'details.html', {'lecturer': lecturer})


def classes(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'classes.html', {'lecturer': lecturer})


def attendance(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'attendance.html', {'lecturer': lecturer})


def qrcode(request):
    if request.method == "POST":
        form = QrRegister(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = QrRegister()
    return render(request, 'qrcode.html', {'form': form},)

def genqrcode(request):
    qrcode = Qrcode.objects.all()
    return render(request, 'genqrcode.html', {'qrcode': qrcode})

def reports(request):
    ams = Ams.objects.all()
    return render(request, 'reports.html', {'ams':ams})


def qrregister(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'qrregister.html', {'lecturer': lecturer})


def responses(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'responses.html', {'lecturer': lecturer})


def timetable(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'timetable.html', {'lecturer': lecturer})


def studsregister(request):
    lecturer = Lecturer.objects.all()
    return render(request, 'studsregister.html', {'lecturer': lecturer})








