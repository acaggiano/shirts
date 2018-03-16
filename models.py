from django.db import models
import datetime

# Create your models here.
class Shirt(models.Model):
    name = models.CharField(max_length=50)
    worn = models.BooleanField(default=False)
    image = models.ImageField(upload_to='uploads/shirts/', blank=True)
    last_worn = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if self.worn:
           self.last_worn = datetime.date.today()
        super().save(*args, **kwargs)
