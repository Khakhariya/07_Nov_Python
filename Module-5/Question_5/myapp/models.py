from django.db import models

# Create your models here.

class postmodel (models.Model):

    name = models.CharField(max_length=10)
    village = models.CharField(max_length=15)
    city = models.CharField(max_length=15)
    pin = models.IntegerField()