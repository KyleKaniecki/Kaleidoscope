from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render,redirect

from django.views.generic import DeleteView,DetailView, View

from .models import Appointment

from .forms import ApptUpdateForm

from django.contrib.auth.models import User

# Create your views here.

class ApptDeleteView(DeleteView):
    model = Appointment
    template_name = "appointments/delete.html"

    success_url = reverse_lazy("Dashboard")

    def post(self, request, *args, **kwargs):
        for user in User.objects.all():
            for nf in user.notifications.unread():
                if nf.target == self.get_object():
                    nf.mark_as_read()
        return super(ApptDeleteView, self).post(request)


class ApptDetailView(DetailView):
    model = Appointment
    template_name = "appointments/detail.html"

    def get(self, request, *args, **kwargs):
        for i in request.user.notifications.unread():
            if i.target == self.get_object():
                i.mark_as_read()
        return super(ApptDetailView, self).get(request)

class ApptUpdateView(View):

    def get(self,request):
        return render(request,'appointments/update.html')

    def post(self,request):
        pass