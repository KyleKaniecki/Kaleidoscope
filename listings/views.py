from django.shortcuts import render,redirect

from django.views.generic import View

from accounts.models import Admin

from .forms import ListingCreateForm

from .models import Listing

# Create your views here.

class ListingCreate(View):

    def get(self,request):
        form = ListingCreateForm(None)
        return render(request,"listings/create.html",{"form":form})



    def post(self,request):
        form = ListingCreateForm(request.POST,request.FILES)

        print(form.errors)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = Admin.objects.get(user=request.user)
            listing.save()
            return redirect("/account/dashboard")

        return render(request, "listings/create.html", {"form": form})

class Doors(View):

    def get(self,request):
        return render(request,"listings/doors.html",{"doors":Listing.objects.filter(category=1)})
