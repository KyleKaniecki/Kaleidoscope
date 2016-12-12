from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):

    recipient = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Recipient")

    sender = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name="Sender",related_name="Sender")

    subject = models.CharField(max_length=50,null=True, blank=True,verbose_name="Subject")

    body = models.TextField(blank=True,null=True,verbose_name="Content")

    read = models.BooleanField(default=False)

