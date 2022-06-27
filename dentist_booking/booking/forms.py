from django.forms import ModelForm, ModelMultipleChoiceField, ModelChoiceField
from django import forms

from booking.models import Appointment, Procedure, Schedule
from users.models import User


class BookingForm(ModelForm):
    procedures = ModelMultipleChoiceField(
        label='Procedures',
        help_text='Maximum 3 procedures per appointment',
        required=True,
        queryset=Procedure.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control form-control-lg'})
    )
    dentist = ModelChoiceField(
        required=True,
        help_text='Choose a doctor',
        queryset=User.objects.filter(groups__name='Doctors'),
        empty_label="Choose a doctor",
        widget=forms.Select(attrs={'class': 'form-control form-control-lg', "placeholder": "Example input"})
    )
    schedule = ModelChoiceField(
        required=True,
        help_text='Doctor available time',
        queryset=Schedule.objects.none(),
        empty_label="Choose a date",
        widget=forms.Select(attrs={'class': 'form-control form-control-lg', "placeholder": "Example input"})
    )

    class Meta:
        model = Appointment
        fields = ['procedures', 'dentist', 'client', 'schedule']




