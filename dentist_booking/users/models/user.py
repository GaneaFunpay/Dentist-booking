from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


class User(AbstractUser):
    phone = PhoneNumberField(null=False, blank=False, unique=True)

    def __str__(self):
        return self.get_full_name()
