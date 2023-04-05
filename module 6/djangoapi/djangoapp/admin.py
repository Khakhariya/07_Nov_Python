from django.contrib import admin
from .models import Book_model

# Register your models here.


class Book_admin (admin.ModelAdmin):

    list_display = ['Title','Author','Isbn','Publisher']

admin.site.register(Book_model,Book_admin)