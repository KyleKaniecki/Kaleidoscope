from django.shortcuts import render,redirect

from django.views.generic import View
from django.views.generic import CreateView, UpdateView

from django.contrib.auth import authenticate, login, logout

from .forms import UserRegistrationForm, ClientRegistrationForm, ClientUpdateForm, LoginForm

from .models import Client

from django.contrib.auth.models import User

# Create your views here.

class Login(View):

    def get(self,request):
        form = LoginForm(request.POST or None)
        return render(request, "accounts/profile/login.html", {"form": form})

    def post(self,request):
        form = LoginForm(request.POST or None)

        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            print("Loggedin")
            return redirect("/loggedin/")

        return redirect("/loggedin/")



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

    def post(self,request):
        title = "Register"
        userform = UserRegistrationForm(request.POST or None,instance=request.user)
        clientform = ClientRegistrationForm(request.POST or None,instance=request.user)

        if clientform.is_valid() and userform.is_valid():
            client = clientform.save(commit=False)
            user = userform.save(commit=False)
            user.set_password(userform.cleaned_data['password'])
            user.save()
            client.user = user
            client.save()
            user = authenticate(username=userform.cleaned_data['username'], password=userform.cleaned_data['password'])

            login(request, user)
            return redirect("/loggedin/")

        return render(request, "accounts/profile/update.html", context={"userform": userform,
                                                                        "clientform": clientform,
                                                                        "title": title})





