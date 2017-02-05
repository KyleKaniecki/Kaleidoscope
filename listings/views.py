from django.shortcuts import render,redirect
from django.core.urlresolvers import reverse_lazy

from django.views.generic import View,DeleteView

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

        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = Admin.objects.get(user=request.user)
            listing.save()
            return redirect("/account/dashboard")

        return render(request, "listings/create.html", {"form": form})

class Doors(View):

    def get(self,request):
        return render(request, "listings/display.html", {"listings":Listing.objects.filter(category=1)})

class Transoms(View):

    def get(self,request):
        return render(request, "listings/display.html",{"listings":Listing.objects.filter(category=2)})


class Cabinets(View):

    def get(self,request):
        return render(request, "listings/display.html",{"listings":Listing.objects.filter(category=3)})

class Miscellaneous(View):

    def get(self,request):
        return render(request, "listings/display.html",{"listings":Listing.objects.filter(category=4)})


class ListingUpdate(View):

    def get(self,request,pk):
        form = ListingCreateForm(None,instance=Listing.objects.get(pk=pk))
        return render(request,'listings/create.html',{'form':form})

    def post(self,request,pk):
        form = ListingCreateForm(request.POST,instance=Listing.objects.get(pk=pk))

        if form.is_valid():
            listing = form.save(commit=False)
            listing.author = Admin.objects.get(user=request.user)
            listing.save()
            return redirect("/listings/doors")

        return render(request, "listings/create.html", {"form": form})


class ListingDelete(DeleteView):

    model = Listing
    template_name = "listings/delete.html"

    success_url = reverse_lazy("DoorsView")

