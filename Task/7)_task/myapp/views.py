from django.shortcuts import render

# Create your views here.

def index (request):
    fr = open('count.txt','r')

    num = int(fr.read())
    
    fr.close()
   
    add(num)
    
    return render(request,'index.html',context={'number' : num})

def add (number):

    number = number + 1

    fl=open('count.txt','w')

    fl.write(f"{number}")

    fl.close()

# ---------------------------------------------------------------------

def customer (request):
    return render(request,'customer.html')

