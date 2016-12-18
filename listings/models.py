from django.db import models

from accounts.models import Admin

# Create your models here.

class Listing(models.Model):

    title = models.CharField(max_length=30)

    author = models.ForeignKey(Admin,on_delete=models.CASCADE)

    image = models.ImageField()

    description = models.TextField(max_length=300)
