from django.contrib import admin
from .models import apimodel

# Register your models here.

class apiadmin (admin.ModelAdmin):

    list_display = ['name','city','email','mobile']

admin.site.register(apimodel,apiadmin)