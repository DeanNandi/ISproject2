from django.contrib import admin
from .models import Student, Registration, Search


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'ID_No', 'email', 'course_enrolled')


admin.site.register(Student, StudentAdmin)


class RegistrationAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'ID_No')


admin.site.register(Registration, RegistrationAdmin)


class SearchAdmin(admin.ModelAdmin):
    list_display = ('unit_name', 'admission')


admin.site.register(Search, SearchAdmin)
