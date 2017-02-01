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
            self.fields['admin'].widget = forms.HiddenInput()
            #self.fields['client'].widget
            self.fields['client'].widget.attrs = {"class": "form-control select-to"}
        else:
            self.fields['client'].widget = forms.HiddenInput()
            self.fields['admin'].widget.attrs = {"class": "form-control"}

        self.fields['start'].widget = forms.TextInput(attrs={"class":"form-control","id":"apptstart"})
        self.fields['duration'].widget = forms.DateTimeInput(attrs={"class":"form-control","id":"apptduration"})
        self.fields['comments'].widget = forms.Textarea(attrs={"class":"form-control"})

    def clean(self):
        form_data = self.cleaned_data
        if form_data['admin']:
            form_data['client'] = Client.objects.get(user=self.user)
        elif form_data['client']:
            form_data['admin'] = Admin.objects.get(user=self.user)
        elif not form_data['admin']:
            self.add_error('admin','This field is required')
        else:
            self.add_error('client','This field is required')

        print(form_data)
        return form_data

class ApptUpdateForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            'start',
            'duration',
            'comments'
        ]

    def __init__(self,*args,**kwargs):
        super(ApptUpdateForm, self).__init__(*args,**kwargs)
        self.fields['start'].widget = forms.TextInput(attrs={"class": "form-control", "id": "apptstart"})
        self.fields['duration'].widget = forms.DateTimeInput(attrs={"class": "form-control", "id": "apptduration"})
        self.fields['comments'].widget = forms.Textarea(attrs={"class": "form-control"})
