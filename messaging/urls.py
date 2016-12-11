from django.conf.urls import url, include

from .views import CreateMessage,Inbox

urlpatterns = [
    url(r'newmessage/$',view=CreateMessage.as_view(),name="CreateMessage"),
    url(r'inbox/$',view=Inbox.as_view(),name="Inbox")

]