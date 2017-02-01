from django.shortcuts import render,redirect

from django.views.generic import View

from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, ClientRegistrationForm, ClientUpdateForm, UserUpdateForm,LoginForm

from .models import Client, Admin

from appointments.models import Appointment
from appointments.forms import AppointmentCreateForm

from listings.models import Listing

from django.contrib.auth.models import User

from notifications.signals import notify

# Create your views here.

class Login(View):

    def get(self,request):
        form = LoginForm(None)
        return render(request, "accounts/client/login.html", {"form": form})

    def post(self,request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password'])
            login(request, user)
            return redirect("/loggedin")

        return render(request, "accounts/client/login.html", {"form": form})

class LogOut(View):

    def get(self,request):
        logout(request)
        return redirect("/")

class Dashboard(View):

    def get(self,request):

        form = AppointmentCreateForm(user=request.user)

        if not request.user.is_staff:
            appointments = Appointment.objects.filter(client = Client.objects.get(user=request.user))
        else:
            appointments = Appointment.objects.filter(admin = Admin.objects.get(user=request.user))

        return render(request,"accounts/admin/dashboard.html",{"form":form,
                                                               "appointments":appointments})

    def post(self,request):

        #print(request.POST)
        form = AppointmentCreateForm(user=request.user,data=request.POST)
        appointments = []

        if form.is_valid():
            appt = form.save(commit=False)
            if request.user.is_staff:
                appt.admin = Admin.objects.get(user=request.user)
                appointments = Appointment.objects.filter(admin=Admin.objects.get(user=request.user))
            else:
                appt.client = Client.objects.get(user=request.user)
                appointments = Appointment.objects.filter(client=Client.objects.get(user=request.user))

            appt.save()
            notify.send(request.user,
                        actor=(appt.admin.user.first_name + " " + appt.admin.user.last_name),
                        recipient=appt.client.user,
                        verb=u"has created an appointment with you",
                        target=appt)

        form = AppointmentCreateForm(user=request.user,data=None)
        return render(request,"accounts/admin/dashboard.html",context={"form":form,
                                                                       "appointments":appointments})


class CheckUser(View):

    def get(self,request):
        listings = Listing.objects.all()
        if Admin.objects.filter(user=request.user):
            return redirect("/account/dashboard")
            #return render(request, "accounts/admin/dashboard.html",context={"listings":listings})
        else:
            return render(request, "home/homepage.html",context={"listings":listings})


def create_client(request):
    title = "Register"
    userform = UserRegistrationForm(request.POST or None)
    clientform = ClientRegistrationForm(request.POST or None)

    if clientform.is_valid() and userform.is_valid():
        client = clientform.save(commit=False)
        user = userform.save(commit=False)
        user.set_password(userform.cleaned_data['password'])
        user.save()
        client.user = user
        client.save()
        user = authenticate(username=userform.cleaned_data['username'],password=userform.cleaned_data['password'])

        login(request,user)
        return redirect("/loggedin/")

    return render(request,"accounts/registration/register.html",context={"userform":userform,
                                                                            "clientform":clientform,
                                                                            "title":title})

class UpdateClient(View):

    title = "Update Profile"

    def get(self,request):
        userform = UserUpdateForm(None,instance=request.user)
        clientform = ClientUpdateForm(None,instance=Client.objects.get(user=request.user))

        return render(request, "accounts/client/update.html", context={"userform": userform,
                                                                        "clientform": clientform,
                                                                        "title": self.title})

    def post(self,request):
        userform = UserUpdateForm(request.POST, instance=request.user)
        clientform = ClientUpdateForm(request.POST, instance=Client.objects.get(user=request.user))

        if clientform.is_valid() and userform.is_valid():
            client = clientform.save(commit=False)
            user = userform.save()
            client.user = user
            client.save()
            return redirect("/loggedin/")

        return render(request, "accounts/client/update.html", context={"userform": userform,
                                                                        "clientform": clientform,
                                                                        "title": self.title})





