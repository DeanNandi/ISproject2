from django.contrib import admin
from .models import Email
from .models import BBIT
from .models import BTC
from .models import ICS


class EmailAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'created_date')


admin.site.register(Email, EmailAdmin)


class BBITAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "ID_No", "group", "unit_name", "course_code", "academic_year")


admin.site.register(BBIT, BBITAdmin)


class BTCAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "ID_No", "group", "unit_name", "course_code", "academic_year")


admin.site.register(BTC, BTCAdmin)


class ICSAdmin(admin.ModelAdmin):
    list_display = ("first_name", "second_name", "ID_No", "group", "unit_name", "course_code", "academic_year")


admin.site.register(ICS, ICSAdmin)
