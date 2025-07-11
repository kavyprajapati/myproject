from django.db import models

# Create your models here.

class contact(models.Model):
    FullName = models.CharField(default= None, max_length=100)
    EmailAddress = models.EmailField(null=True, blank=True)
    ContactNumber = models.IntegerField(null=True, blank=True)
    YourMessage = models.TextField(null=True, blank=True)
