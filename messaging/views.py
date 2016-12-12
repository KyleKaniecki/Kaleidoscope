from django.shortcuts import render,redirect

from django.views.generic import View,DetailView

from .forms import MessageCreateForm

from .models import Message

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

            return

        return render(request,"messages/create.html",context={"form":form})


class Inbox(View):

    def get(self,request):

        form = MessageCreateForm(None)

        messages = Message.objects.filter(recipient=request.user)

        return render(request,"messages/inbox.html",context={"form":form,
                                                             "messages":messages})

    def post(self,request):

        form = MessageCreateForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.sender = request.user
            message.save()


        form = MessageCreateForm(None)

        messages = Message.objects.filter(recipient=request.user)

        return render(request,"messages/inbox.html",context={"form":form,
                                                             "messages":messages})

class MessageDetail(DetailView):

    model = Message

    template_name = "messages/detail.html"




