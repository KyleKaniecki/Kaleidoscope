from django.conf.urls import url, include

from .views import CreateMessage,Inbox, MessageDetail

urlpatterns = [
    url(r'newmessage/$',view=CreateMessage.as_view(),name="CreateMessage"),
    url(r'inbox/$',view=Inbox.as_view(),name="Inbox"),
    url(r'message/(?P<pk>[0-9]+)/$',view=MessageDetail.as_view(),name="MessageDetails")

]