from django import forms
from django.contrib.auth.models import User

from .models import Message

class MessageCreateForm(forms.ModelForm):

    class Meta:
        model = Message

        fields = [
            'recipient',
            'subject',
            'body'
        ]

    def __init__(self,*args,**kwargs):
        super(MessageCreateForm, self).__init__(*args,**kwargs)

        self.fields['recipient'] = forms.ModelChoiceField(queryset=User.objects.all(),widget=forms.Select(attrs={'class':"form-control"}))
        self.fields['subject'].widget = forms.TextInput(attrs={"class":"form-control"})
        self.fields['body'].widget = forms.Textarea(attrs={"class": "form-control","style":"resize:none"})

