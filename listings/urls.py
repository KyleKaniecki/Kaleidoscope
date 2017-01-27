from django.conf.urls import url

from .views import ListingCreate, Doors

urlpatterns = [
    url(r'^create/$',ListingCreate.as_view(),name="ListingCreate"),
    url(r'^doors/$',Doors.as_view(), name="DoorsView")
]