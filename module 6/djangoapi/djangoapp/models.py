from django.db import models
from datetime import datetime

# Create your models here.

class Book_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    Title = models.CharField(max_length=50)
    Author = models.CharField(max_length=50)
    Isbn = models.CharField(max_length=120)
    Publisher = models.CharField(max_length=120)