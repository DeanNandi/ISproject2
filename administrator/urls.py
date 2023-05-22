from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.admin),
    path('administrator.html', views.admin),
    path('administrator', views.admin, name='administrator'),
    path('admininfo', views.admin_info, name='admininfo'),
    path('lecturerpage', views.lecturer_page, name='lecturerpage'),
    path('mainpage', views.main_page, name='home'),
    path('landing.html', views.landing),
    path('timetable.html', views.timetable),
    path('departments', views.depart, name='departments'),
    path('newsletter', views.newsletter, name='newsletter'),
    path(r'bbit-form', views.bbit_register, name='bbit-form'),
    path(r'btc-form', views.btc_register, name='btc-form'),
    path(r'ics-form', views.ics_register, name='ics-form'),
    # path('lecturer-report', views.lec_reports, name='lecturer-report'),
    path('class-assignment', views.class_assign, name='class-assignment'),
    path('register-admin/', views.registerPage, name="register-admin/"),
	path('login-admin/', views.loginPage, name="login-admin/"),
	path('logout-admin/', views.logoutUser, name="logout-admin/"),
    path('bbit-report', views.bbit_reports, name='bbit-report'),
    path('btc-report', views.btc_reports, name='btc-report'),
    path('ics-report', views.ics_reports, name='ics-report'),
    # path('department-report', views.class_ics, name='department-report')

]