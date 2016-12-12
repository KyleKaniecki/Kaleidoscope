from django.contrib import admin

from .models import Client,Admin

# Register your models here.

class ClientAdminConsole(admin.ModelAdmin):
    fields = ('user','address','city','state','zip_code')
    list_display = ('user','address','city','state','zip_code')


class AdminAdminConsole(admin.ModelAdmin):
    fields = ('user', 'address', 'city', 'state', 'zip_code')
    list_display = ('user', 'address', 'city', 'state', 'zip_code')



admin.site.register(Client,ClientAdminConsole)
admin.site.register(Admin,AdminAdminConsole)