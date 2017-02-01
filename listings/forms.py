from django import forms

from .models import Listing

class ListingCreateForm(forms.ModelForm):

    class Meta:

        model = Listing

        fields = [
            'title',
            'image',
            'description',
            'category',
            'consultation'
        ]

    def __init__(self,*args,**kwargs):
        super(ListingCreateForm, self).__init__(*args,**kwargs)

        self.fields['title'].widget = forms.TextInput(attrs={"class":"form-control", "type":"text"})
        self.fields['image'].widget = forms.FileInput(attrs={"class":"form-control"})
        self.fields['description'].widget = forms.Textarea(attrs={"class" : "form-control"})
        self.fields['category'].widget.attrs = {"class":"form-control"}
        self.fields['consultation'].label = "Consultation required?"