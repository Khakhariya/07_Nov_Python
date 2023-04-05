from django.db import models
from datetime import datetime

# Create your models here.

class apimodel (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    name =models.CharField(max_length=20)
    city =models.CharField(max_length=20)
    email =models.EmailField()
    mobile =models.BigIntegerField()