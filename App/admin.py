from django.contrib import admin
from .models import Event
from .models import Nomination

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['academicyear', 'eventname', 'eventfocus', 'eventstartdate',
                    'eventenddate', 'eventvenue', 'eventresourceperson', 'starttime', 'endtime']
    list_editable = ['academicyear']
    list_display_links = ['eventname']
    search_fields = ['eventname']


@admin.register(Nomination)
class NominationAdmin(admin.ModelAdmin):
    list_display = ["EmployeeName", "EmployeeId", "Branch", "FunctionDepartment", "ContactNo",
                    "ContactNoMobile", "ReportingAuthority", "TotalExperience", "TotalTeachingExperience", "Batch"]
