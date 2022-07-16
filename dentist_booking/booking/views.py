import datetime

from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from booking.forms import BookingForm
from booking.models import Schedule, Appointment, Procedure
from booking.tasks import notify_dentist


class IndexView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


@method_decorator(login_required, name='dispatch')
class BookingView(View):
    form_class = BookingForm
    template_name = 'booking/booking.html'

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        data = {
            'dentist_id': request.POST.get('dentist'),
            'schedule_id': request.POST.get('schedule'),
            'client_id': request.user.id
        }
        try:
            appointment = Appointment.objects.create(**data)
            appointment.schedule_id = data.get('schedule_id')
            appointment.save()

            procedures = list(procedure for procedure in Procedure.objects.filter(id__in=request.POST.get('procedures')))
            for procedure in procedures:
                appointment.procedures.add(procedure)
            Schedule.objects.filter(id=data.get('schedule_id')).update(status='occupied')
            notify_dentist(
                client=f'{appointment.client.get_full_name()}',
                dentist=f'{appointment.dentist.email}',
                verbose_name="notify_dentist",
                schedule=appointment.schedule.start_time - datetime.timedelta(days=1)
            )

            return render(request, self.template_name, {'form': self.form_class, 'success': True})
        except Exception as e:
            print(e)
            form = self.form_class(data)
            return render(request, self.template_name, {'form': form})


@csrf_exempt
def get_schedule(request):
    dentist = request.POST.get('dentist', None)
    sub_category = list(
        {'id': schedule.id, 'value': str(schedule.start_time.strftime("%Y-%m-%d %H:%M:%S"))}
        for schedule in Schedule.objects.filter(dentist_id=dentist, status='pending')
    )
    return JsonResponse(sub_category, safe=False)
