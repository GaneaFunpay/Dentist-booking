from django.conf import settings
from django.contrib.auth.views import LogoutView
from django.urls import path

from users.api.views.account_activation import activate
from users.api.views.sign_in import SignInView
from users.api.views.sign_up import SignUpView


app_name = 'users'
urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),
    path('signin', SignInView.as_view(), name='signin'),
    path('logout/', LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate'),
]
