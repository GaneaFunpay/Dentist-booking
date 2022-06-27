
from django.db import models
from django.db.models import Q

from users.models import User


class Procedure(models.Model):
    name = models.CharField(max_length=64)
    required_time = models.TimeField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name


class Schedule(models.Model):
    statuses = (
        ('pending', 'Pending'),
        ('occupied', 'Occupied'),
    )
    status = models.CharField(
        max_length=64,
        choices=statuses,
        default='pending'
    )
    dentist = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='dentist_schedules',
        limit_choices_to=Q(groups__name='Doctors')
    )
    start_time = models.DateTimeField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return str(self.start_time)


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
