from django.contrib import admin
from django.urls import path
from apiapp import views

urlpatterns = [
    path('', views.index),
    path('showalldata/', views.apiweb),
    path('getdata/<int:id>/', views.get_specific_data),
    path('adddata/', views.adddata),
    path('deletedata/<int:id>/', views.deletedata),
    path('updatedata/<int:id>/',views.updatedata),
]
