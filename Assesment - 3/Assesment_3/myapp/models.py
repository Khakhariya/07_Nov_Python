from django.db import models
from datetime import datetime

# Create your models here.

class chairmans_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class events_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    event_name =models.CharField(max_length=100)
    event_time = models.DateField()
    event_img = models.FileField(upload_to='static/upload')
    event_information = models.TextField()
    comments = models.TextField()

class notices_view_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class notices_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    notice_title =models.CharField(max_length=100)
    notice_img = models.FileField(upload_to='static/upload')
    notice = models.TextField()
    comments = models.TextField()

class user_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)

class watchmans_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    cate = models.CharField(max_length=15,default='Watchman',blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.EmailField(max_length=50)
    password = models.CharField(max_length=12)
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    Mobile = models.BigIntegerField()

    
class signup_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    cate = models.CharField(max_length=15,default='User')
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=12)
    mail = models.EmailField()

class members_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    cate = models.CharField(max_length=15,default='Member',blank=True)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    username = models.EmailField(max_length=50)
    password = models.CharField(max_length=12)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    Mobile = models.BigIntegerField()
    bhk = models.IntegerField(default=2)


class visitors_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    name = models.CharField(max_length=50)
    vehicle_no = models.CharField(max_length=50)
    total_visitor = models.IntegerField()
    visit_house_no = models.CharField(max_length=15)
    out_time = models.CharField(max_length=50,blank=True)

class transactions_model (models.Model):

    created = models.DateTimeField(default=datetime.now(),blank=True)
    rate = models.IntegerField()
    maintenance_rate = models.IntegerField()
    parking = models.IntegerField()
    event_fund = models.IntegerField()
    event = models.CharField(max_length=100)
