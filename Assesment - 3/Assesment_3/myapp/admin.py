from django.contrib import admin
from .models import signup_model,members_model

# Register your models here.

class signup_admin (admin.ModelAdmin):

    list_display = ['username','password']

class members_admin (admin.ModelAdmin):

    list_display = ['firstname','lastname','username','password','city','state','Mobile']

admin.site.register(signup_model,signup_admin)
admin.site.register(members_model,members_admin)