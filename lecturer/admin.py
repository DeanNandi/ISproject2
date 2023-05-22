from django.contrib import admin
from .models import Lecturer
from .models import Qrcode
from .models import Ams
from .models import Unitregister
from import_export.admin import ImportExportModelAdmin

class LecturerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', 'ID_No', 'phone_No', 'email', 'unit_name', 'academic_year')


admin.site.register(Lecturer, LecturerAdmin)


class QrcodeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'second_name', "unit_name", "group_year", "qr_generator", "form_generator", "edit_link", "responses_link",)


admin.site.register(Qrcode, QrcodeAdmin)


@admin.register(Ams)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('id','timestamp', 'email_address', 'first_name', 'second_name', 'admission')
    pass


@admin.register(Unitregister)
class ViewAdmin(ImportExportModelAdmin):
    list_display = ('id',"timestamp", "email_address", "first_name", "second_name","admission","unit_name", "group",
                  "lec_first_name", "lec_second_name")
    pass

