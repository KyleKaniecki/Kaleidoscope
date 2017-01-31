from django.shortcuts import render,redirect

from django.views.generic import View

from listings.models import Listing


class Home(View):

    def get(self,request):
        listings = Listing.objects.all()
        return render(request,"home/homepage.html",{"listings": listings})

class Contact(View):

    def get(self,request):
        return render(request, "home/contact.html")
