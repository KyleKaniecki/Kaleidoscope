from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from .views import ListingCreate, Doors, Transoms, Miscellaneous, Cabinets, ListingUpdate,ListingDelete

urlpatterns = [
    url(r'^create/$',ListingCreate.as_view(),name="ListingCreate"),
    url(r'^doors/$',Doors.as_view(), name="DoorsView"),
    url(r'^transoms/$',Transoms.as_view(),name="TransomsView"),
    url(r'^cabinets/$',Cabinets.as_view(),name="CabinetsView"),
    url(r'^miscellaneous/$',Miscellaneous.as_view(),name="MiscellaneousView"),
    url(r'^update/(?P<pk>[0-9]+)/$',ListingUpdate.as_view(),name="ListingUpdate"),
    url(r'^delete/(?P<pk>[0-9]+)/$',ListingDelete.as_view(),name="ListingDelete")
]