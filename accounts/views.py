from django.shortcuts import render,redirect

from django.views.generic import View
from django.views.generic import CreateView

from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, ClientRegistrationForm, ClientUpdateForm, LoginForm

from .models import Client

from django.contrib.auth.models import User

# Create your views here.

class Login(View):

    def get(self,request):
        form = LoginForm(None)
        return render(request, "accounts/profile/login.html", {"form": form})

    def post(self,request):
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(username=form.data['username'], password=form.data['password'])
            login(request, user)
            return redirect("/loggedin")

        return render(request, "accounts/profile/login.html", {"form": form})

class LogOut(View):

    def get(self,request):
        logout(request)
        return redirect("/")

class CheckUser(View):

    def get(self,request):
        return render(request,"home/loggedin.html")

    def post(self,request):
        return render(request, "home/loggedin.html")

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

class UpdateUser(View):

    title = "Update Profile"

    def get(self,request):
        userform = UserRegistrationForm(None,instance=request.user)
        clientform = ClientRegistrationForm(None,instance=Client.objects.get(user=request.user))

        return render(request, "accounts/profile/update.html", context={"userform": userform,
                                                                        "clientform": clientform,
                                                                        "title": self.title})

    def post(self,request):
        userform = UserRegistrationForm(request.POST, instance=request.user)
        clientform = ClientRegistrationForm(request.POST, instance=Client.objects.get(user=request.user))

        if clientform.is_valid() and userform.is_valid():
            client = clientform.save(commit=False)
            user = userform.save()
            client.user = user
            client.save()
            return redirect("/loggedin/")

        return render(request, "accounts/profile/update.html", context={"userform": userform,
                                                                        "clientform": clientform,
                                                                        "title": self.title})





