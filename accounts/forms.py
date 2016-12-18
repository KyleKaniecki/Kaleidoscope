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

    def __init__(self,*args,**kwargs):
        super(UserRegistrationForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['email'].widget = forms.EmailInput(attrs={"class": "form-control"})
        self.fields['password'].widget = forms.PasswordInput(attrs={"class": "form-control"})
        self.fields['first_name'].widget = forms.TextInput(attrs={"class": "form-control"})
        self.fields['last_name'].widget = forms.TextInput(attrs={"class": "form-control"})


class UserUpdateForm(forms.ModelForm):

    class Meta:

        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name'
        ]

    def __init__(self,*args,**kwargs):
        super(UserUpdateForm, self).__init__(*args,**kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['email'].widget = forms.EmailInput(attrs={"class": "form-control"})
        self.fields['first_name'].widget = forms.TextInput(attrs={"class": "form-control"})
        self.fields['last_name'].widget = forms.TextInput(attrs={"class": "form-control"})

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

    def __init__(self,*args,**kwargs):
        super(ClientRegistrationForm, self).__init__(*args,**kwargs)
        self.fields['address'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['city'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['state'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['zip_code'].widget = forms.TextInput(attrs={"class":"form-control"})


class ClientUpdateForm(forms.ModelForm):

    class Meta:
        model = Client

        fields = [
            'address',
            'city',
            'state',
            'zip_code'
        ]

    def __init__(self,*args,**kwargs):
        super(ClientUpdateForm, self).__init__(*args,**kwargs)
        self.fields['address'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['city'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['state'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['zip_code'].widget = forms.TextInput(attrs={"class":"form-control"})


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
        self.fields['password'].widget = forms.PasswordInput(attrs={"class":"form-control"})
        self.fields['username'].widget = forms.TextInput(attrs={"class":"form-control"})

    def is_valid(self):
        user = authenticate(username=self.data['username'],password=self.data['password'])
        if user is not None:
            return True
        return False

