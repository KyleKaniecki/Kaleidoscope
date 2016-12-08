from django.conf.urls import url

from .views import create_client,Login,UpdateUser

urlpatterns = [
    url(r'^register/$',view=create_client,name="ClientRegister"),
    url(r'^update/$',view=UpdateUser.as_view(),name="ClientUpdate"),
]