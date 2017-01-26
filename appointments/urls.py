from django.conf.urls import url, include

from .views import ApptDeleteView, ApptDetailView

urlpatterns = [
    url(r'^delete/(?P<pk>[0-9]+)/$', ApptDeleteView.as_view(),name="ApptDeleteView"),
    url(r'^detail/(?P<pk>[0-9]+)/$', ApptDetailView.as_view(), name="ApptDetailView")
]