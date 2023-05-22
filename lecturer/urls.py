from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from lecturer.views import UploadView
from lecturer.views import UploadViews

urlpatterns = [
    path('', views.index),
    path("index2.html", views.index2, name="homepage"),
    path('index.html', views.index),
    path('details.html', views.details),
    path('classes.html', views.classes),
    path('attendance.html', views.attendance),
    path('qrcode.html', views.qrcode),
    path('qrcode-generate', views.genqrcode, name="qrcode-generate"),
    path('qrregister.html', views.qrregister),
    path('timetable.html', views.timetable),
    path('login.html', views.login),
    path("register", views.register, name="register"),
    path('login', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('studsregister.html', views.studsregister),
    path(r'form', views.lec_register, name='form'),
    # path("register", views.register, name="register"),
    path('LecRegister', views.lec_register, name='LecRegister'),
    path('home', views.home, name='home'),
    path('create-post', views.create_post, name='create-post'),
    path('upload/', UploadView.as_view()),
    path('reports-lecs', views.reports, name='reports-lecs'),
    path('upload-students/', UploadViews.as_view()),

]