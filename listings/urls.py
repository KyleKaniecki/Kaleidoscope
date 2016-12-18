from django.conf.urls import url

from .views import ListingCreate

urlpatterns = [
    url(r'^create/$',ListingCreate.as_view(),name="ListingCreate")

]