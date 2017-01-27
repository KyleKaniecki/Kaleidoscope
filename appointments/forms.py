from django import forms
from .models import Appointment
from accounts.admin import Client, Admin



class AppointmentCreateForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            'client',
            'admin',
            'start',
            'duration',
            'comments'
        ]

    def __init__(self,user,*args,**kwargs):
        self.user = user
        super(AppointmentCreateForm, self).__init__(*args,**kwargs)
        if self.user.is_staff:
            self.fields['admin'].value = Admin.objects.get(user=self.user)
            self.fields['admin'].widget = forms.HiddenInput()
            self.fields['client'].widget.attrs = {"class": "form-control"}
        else:
            self.fields['client'].value = Client.objects.get(user=self.user)
            self.fields['client'].widget = forms.HiddenInput()
            self.fields['admin'].widget.attrs = {"class": "form-control"}

        self.fields['start'].widget = forms.TextInput(attrs={"class":"form-control","id":"apptstart"})
        self.fields['duration'].widget = forms.DateTimeInput(attrs={"class":"form-control","id":"apptduration"})
        self.fields['comments'].widget = forms.Textarea(attrs={"class":"form-control"})

    def is_valid(self):
        return super(AppointmentCreateForm, self).is_valid()