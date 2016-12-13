from django.shortcuts import render,redirect

from django.views.generic import View
from django.views.generic import CreateView

from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, ClientRegistrationForm, ClientUpdateForm, UserUpdateForm,LoginForm

from messaging.forms import MessageCreateForm

from .models import Client, Admin

from appointments.models import Appointment
from appointments.forms import AppointmentCreateForm

from django.contrib.auth.models import User

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

        form = AppointmentCreateForm()

        appointments = Appointment.objects.filter(admin = Admin.objects.get(user=request.user))

        return render(request,"accounts/admin/dashboard.html",{"form":form,
                                                               "appointments":appointments})

    def post(self,request):
        form = AppointmentCreateForm(request.POST)

        if form.is_valid():
            appt = form.save(commit=False)
            appt.admin = Admin.objects.get(user = request.user)
            appt.save()

        form = AppointmentCreateForm(None)

        appointments = Appointment.objects.filter(admin=Admin.objects.get(user=request.user))


        return render(request,"accounts/admin/dashboard.html",context={"form":form,
                                                                       "appointments":appointments})



class CheckUser(View):

    def get(self,request):
        if Admin.objects.filter(user=request.user):
            return render(request, "accounts/admin/loggedin.html")
        else:
            return render(request, "accounts/client/loggedin.html")

    def post(self,request):
        return render(request, "accounts/admin/loggedin.html")

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





