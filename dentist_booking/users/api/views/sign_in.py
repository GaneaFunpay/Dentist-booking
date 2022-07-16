from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

from users.api.forms.login import LoginForm


class SignInView(LoginView):
    form_class = LoginForm
    template_name = 'users/signin.html'

    def get_success_url(self):
        return reverse_lazy('booking')
