from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy

from django.views.generic import DeleteView

from .models import Appointment

# Create your views here.

class ApptDeleteView(DeleteView):
    model = Appointment
    template_name = "appointments/delete.html"

    success_url = reverse_lazy("Dashboard")
