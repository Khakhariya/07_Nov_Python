from django.db import models

# Create your models here.

class Product_mst_table (models.Model):

    Product_name = models.CharField(max_length=50)
    Product_model = models.CharField(max_length=10)
    Product_price = models.IntegerField()
    Product_image = models.ImageField(upload_to='static/images')
    Product_ram = models.CharField(max_length=20,default='null')
    Product_details = models.TextField(default='none')
    