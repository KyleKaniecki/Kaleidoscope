from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .models import Client


#-------------------User Forms--------------------------
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

class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]

#-------------------Client Forms--------------------------


class ClientRegistrationForm(forms.ModelForm):

    class Meta:
        model = Client
        fields = [
            'address',
            'city',
            'state',
            'zip_code'
        ]


class ClientUpdateForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = [
            'address',
            'city',
            'state',
            'zip_code'
        ]


#-------------------Login Forms--------------------------

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'username',
            'password'
        ]

    def __init__(self,*args,**kwargs):
        super(LoginForm, self).__init__(*args,**kwargs)
        self.fields['password'].widget = forms.PasswordInput()

    def is_valid(self):
        user = authenticate(username=self.data['username'],password=self.data['password'])
        if user is not None:
            return True
        return False

