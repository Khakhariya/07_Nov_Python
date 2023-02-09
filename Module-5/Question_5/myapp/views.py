from django.shortcuts import render,HttpResponse
from .forms import postform

# Create your views here.

def index (request):
    if request.method == 'POST':
        data = postform(request.POST)
        if data.is_valid():
            data.save()
            print('Data has been posted')
            message = 'Data successfully inserted.'
            return HttpResponse (message)
        else :
            print (data.errors)
    return render (request,'index.html')