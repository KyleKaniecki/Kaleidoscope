"""Kaleidoscope URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from home.views import Home, Contact

from accounts.views import Login,CheckUser, LogOut

from django.conf import settings

from django.conf.urls.static import static

import notifications.urls

urlpatterns = [
    url(r'^$',view= Home.as_view(), name="HomePage"),
    url(r'^account/',include('accounts.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$',view=Login.as_view(),name="Login"),
    url(r'^loggedin/$', view=CheckUser.as_view(), name="Loggedin"),
    url(r'^logout/$',view=LogOut.as_view(),name="Logout"),
    url(r'^messaging/', include('messaging.urls')),
    url(r'^listings/', include('listings.urls')),
    url(r'^appointment/',include('appointments.urls')),
    url('^notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^contact/$',Contact.as_view(),name="Contact")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
