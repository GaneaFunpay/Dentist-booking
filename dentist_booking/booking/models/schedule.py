from django.db import models
from django.db.models import Q

from users.models import User


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
