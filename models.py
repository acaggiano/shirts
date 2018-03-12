from django.db import models

# Create your models here.
class Shirt(models.Model):
    name = models.CharField(max_length=50)
    worn = models.BooleanField(default=False)
