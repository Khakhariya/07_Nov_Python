from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path ('',views.index),
    path ('about/',views.about),
    path ('blog/',views.blog),
    path ('contact/',views.contact),
    path ('depatments/',views.depatments),
    path ('doctor/',views.doctor),
]
