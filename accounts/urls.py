from django.conf.urls import url

from .views import create_client,UpdateClient,Dashboard

urlpatterns = [
    url(r'^register/$',view=create_client,name="ClientRegister"),
    url(r'^update/$',view=UpdateClient.as_view(),name="ClientUpdate"),
    url(r'^dashboard/$',view=Dashboard.as_view(),name="Dashboard")
]