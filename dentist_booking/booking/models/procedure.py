from django.db import models


class Procedure(models.Model):
    name = models.CharField(max_length=64)
    required_time = models.TimeField()

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return self.name
