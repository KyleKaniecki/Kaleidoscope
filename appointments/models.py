from django.db import models

from django.contrib.auth.models import User

from accounts.models import Client,Admin

# Create your models here.

class Appointment(models.Model):

    client = models.ForeignKey(Client,on_delete=models.CASCADE,related_name="appointmentClient",blank=True)
    admin = models.ForeignKey(Admin,on_delete=models.CASCADE,related_name="appointmentAdmin",blank=True)

    start = models.DateTimeField()
    duration = models.TimeField()

    comments = models.TextField(max_length=160,blank=True,null=True)

    def __str__(self):
        return ""
