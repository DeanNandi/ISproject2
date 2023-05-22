from django. urls import path
from . import views

urlpatterns = [
    path('', views.studenthome),
    path('student-home', views.studenthome, name='student-home'),
    path('get-qr-code', views.getqr, name='get-qr-code'),
    path('student-landing-page', views.student, name='student-landing-page'),
    path('registration.html', views.my_form),
    path('register-student/', views.registerStudent, name="register-student/"),
	path('login-student/', views.loginStudent, name="login-student/"),
	path('logout-student/', views.logoutStudent, name="logout-student/"),
    path('get-qr-code', views.report_student, name='get-qr-code'),
    path('get-registration', views.getatt, name='get-registration')


]