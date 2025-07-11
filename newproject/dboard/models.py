# models.py
from django.db import models

class AdminUserMaster(models.Model):
    mstName = models.CharField(max_length=100, unique=True)
    mstEmail = models.EmailField(unique=True)
    mstPassword = models.CharField(max_length=100)
    mstStatus = models.BooleanField(default=True)

class cats(models.Model):
    Cate_name = models.CharField(max_length=20)
    cate_image = models.ImageField(upload_to="category_images")
    cate_status = models.BooleanField(default=True)
    cateslug = models.SlugField(null=True, blank=True)
