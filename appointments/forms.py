from django import forms
from .models import Appointment



class AppointmentCreateForm(forms.ModelForm):

    class Meta:
        model = Appointment
        fields = [
            'client',
            'start',
            'duration',
            'comments'
        ]

    def __init__(self,*args,**kwargs):
        super(AppointmentCreateForm, self).__init__(*args,**kwargs)

        self.fields['client'].widget.attrs = {"class":"form-control"}
        self.fields['start'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['duration'].widget = forms.DateTimeInput(attrs={"class":"form-control"})
        self.fields['comments'].widget = forms.Textarea(attrs={"class":"form-control"})