from django.shortcuts import render

# Create your views here.

def url(request) :
    return render(request,'url.html')