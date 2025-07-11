from django.db import models

# Create your models here.

class car(models.Model):
    name = models.CharField(default= None, max_length=100)
    price = models.IntegerField(default=True)
    image = models.ImageField(upload_to='cars')

    def __str__(self):
        return self.name