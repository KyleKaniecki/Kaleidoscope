from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Message(models.Model):

    recipient = models.ForeignKey(User, on_delete=models.CASCADE, name="Recipient",verbose_name="Recipient")

    sender = models.ForeignKey(User, on_delete=models.CASCADE,name="Sender",verbose_name="Sender",related_name="Sender")

    subject = models.CharField(max_length=50,null=True, blank=True,name="Subject",verbose_name="Subject")

    body = models.TextField(blank=True,null=True,name="Content",verbose_name="Content")

