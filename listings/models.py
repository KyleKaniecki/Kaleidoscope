from django.db import models

from accounts.models import Admin

# Create your models here.

CATEGORIES = ((1,"Door"),
              (2,"Transom"),
              (3,"Cabinet"),
              (4,"Miscellaneous"))

class Listing(models.Model):

    title = models.CharField(max_length=30)

    author = models.ForeignKey(Admin,on_delete=models.CASCADE)

    image = models.FileField(upload_to="")

    description = models.TextField(max_length=300)

    category = models.IntegerField(choices=CATEGORIES,default=1)

    consultation = models.BooleanField(default=False)
