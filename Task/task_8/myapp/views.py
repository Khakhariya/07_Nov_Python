from django.shortcuts import render

# Create your views here.

def index (request):
    return render (request, 'index.html')

def about (request):
    return render (request, 'about.html')

def blog (request):
    return render (request, 'blog.html')

def contact (request):
    return render (request, 'contact.html')

def depatments (request):
    return render (request, 'depatments.html')

def doctor (request):
    return render (request, 'doctor.html')