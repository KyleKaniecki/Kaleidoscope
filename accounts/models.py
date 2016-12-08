from django.db import models

from django.contrib.auth.models import User


# Create your models here.

class Client(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE)
    address = models.CharField(max_length=40,blank=True,null=True)
    city = models.CharField(max_length=30,blank=True, null=True)
    state=models.CharField(max_length=20,blank=True,null=True)
    zip_code = models.IntegerField(blank=True,null=True)


class Admin(Client):
    pass
