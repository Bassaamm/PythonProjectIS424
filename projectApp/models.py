from django.db import models

class user(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
# Create your models here.
class services(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=30)
    price = models.CharField(max_length=30)
    image = models.CharField(max_length=30)
    category = models.CharField(max_length=30)