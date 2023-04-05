from django.contrib import admin
from django.urls import path,include
from djangoapp import views

urlpatterns = [
    path ('displaydata/',views.displaydata),
    path ('insertdata/',views.insertdata),
    path ('fetchdata/<int:id>/',views.fetchdata),
    path ('deletedata/<int:id>/',views.deletedata),
    path ('updatedata/<int:id>/',views.updatedata),
]