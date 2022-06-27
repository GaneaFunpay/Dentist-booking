from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from users.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label='First name',
        max_length=30,
        required=True,
        help_text='Enter your first name',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    last_name = forms.CharField(
        label='Last name',
        max_length=30,
        required=True,
        help_text='Enter your last name',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    username = forms.CharField(
        label='Username',
        max_length=30,
        required=True,
        help_text='Enter your username',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    email = forms.EmailField(
        label='Email',
        max_length=30,
        required=True,
        help_text='Enter your email',
        widget=forms.EmailInput(attrs={'class': 'form-control form-control-lg'})
    )
    phone = forms.CharField(
        label='Phone number',
        required=True,
        help_text='Enter your prone number',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    password1 = forms.CharField(
        label='Password',
        required=True,
        help_text='Enter your password',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )
    password2 = forms.CharField(
        label='Confirm password',
        required=True,
        help_text='Confirm your password',
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'phone', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'})
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-lg'})
    )

