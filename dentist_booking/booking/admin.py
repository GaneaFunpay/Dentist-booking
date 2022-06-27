from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin
from import_export.fields import Field
from import_export.widgets import DateTimeWidget
from rangefilter.filters import DateRangeFilter
from import_export import resources
from booking.models import Procedure, Appointment, Schedule


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'required_time')
    search_fields = ['name']
    pass


class AppointmentResource(resources.ModelResource):
    dentist_first_name = Field(attribute='dentist__last_name', column_name='Dentist first name')
    dentist_last_name = Field(attribute='dentist__last_name', column_name='Dentist last name')
    client_first_name = Field(attribute='client__last_name', column_name='Client first name')
    client_last_name = Field(attribute='client__last_name', column_name='Client last name')
    end = Field(attribute='schedule__start_time', column_name='Start time', widget=DateTimeWidget())

    class Meta:
        model = Appointment
        exclude = (
            'id',
            'dentist',
            'client',
            'schedule',
        )


@admin.register(Appointment)
class AppointmentAdmin(ImportExportActionModelAdmin):
    list_display = ('schedule', 'client', 'get_procedures')
    list_filter = (('schedule__start_time', DateRangeFilter),)
    resource_class = AppointmentResource

    def get_queryset(self, request):
        appointments = Appointment.objects.all()
        if request.user.is_superuser:
            return appointments
        return appointments.filter(dentist=request.user)

    def get_procedures(self, obj):
        return "\n".join([p.name for p in obj.procedures.all()])


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('status', 'start_time')
    list_filter = ('status', )

    def get_queryset(self, request):
        schedules = Schedule.objects.all()
        if request.user.is_superuser:
            return schedules
        return schedules.filter(dentist=request.user)
