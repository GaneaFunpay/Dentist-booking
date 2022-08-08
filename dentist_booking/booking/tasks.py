from background_task import background
from django.conf import settings
from django.core.mail import send_mail


@background()
def notify_dentist(client, dentist_email):
    send_mail(
        'One day before notify',
        f'Remind you that you have an appointment with {client}, at ',
        settings.EMAIL_HOST_USER,
        [dentist_email],
    )
