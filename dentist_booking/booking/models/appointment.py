from django.db import models
from django.db.models import Q

from .procedure import Procedure
from .schedule import Schedule
from users.models import User


class Appointment(models.Model):
    dentist = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dentist_appointments',
        limit_choices_to=Q(groups__name='Doctors')
    )
    schedule = models.OneToOneField(
        Schedule,
        default=None,
        on_delete=models.CASCADE,
        related_name='schedule_appointment',
    )
    client = models.ForeignKey(User, on_delete=models.CASCADE, related_name='client_appointments')
    procedures = models.ManyToManyField(Procedure)

    class Meta:
        ordering = ['pk']
