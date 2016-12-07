from django.conf.urls import url

from .views import create_client,Login,UpdateView

urlpatterns = [
    url(r'^register/$',view=create_client,name="ClientRegister"),
    url(r'^update/$',view=UpdateView.as_view(),name="ClientUpdate")
]