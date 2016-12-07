from django import forms
from django.contrib.auth.models import User

from .models import Client

class UserRegistrationForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'password',
            'first_name',
            'last_name'
        ]


class ClientRegistrationForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = [
            'address',
            'city',
            'state',
            'zip_code'
        ]


class ClientUpdateForm(forms.Form):

    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    address = forms.CharField()
    city = forms.CharField()
    state = forms.CharField()
    zip_code = forms.IntegerField()


class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

