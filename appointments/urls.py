from django.conf.urls import url, include

from .views import ApptDeleteView

urlpatterns = [
    url(r'^delete/(?P<pk>[0-9]+)/$', ApptDeleteView.as_view(),name="ApptDeleteView")
]