from django.shortcuts import render,redirect

from django.views.generic import View

from .forms import MessageCreateForm

# Create your views here.

class CreateMessage(View):

    def get(self,request):

        form = MessageCreateForm(None)
        return render(request, "messages/create.html",context={"form":form})

    def post(self,request):
        form = MessageCreateForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()

            return redirect("/inbox")

        return render(request,"messages/create.html",context={"form":form})


class Inbox(View):

    def get(self,request):

        return render(request,"messages/inbox.html",context={})



