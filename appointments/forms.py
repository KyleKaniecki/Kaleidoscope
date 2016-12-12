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

        #self.fields['start'].widget