from django.shortcuts import render,redirect
from .forms import ImageForm
from .models import Product_mst_table

# Create your views here.

def index (request):

    if request.method == 'POST':

        Prod = request.POST['search']

        Prod_id = Product_mst_table.objects.get(Product_name=Prod)

        verify = Product_mst_table.objects.filter(Product_name=Prod)

        if verify :
            
            request.session['pid'] = Prod_id.id

            uid = request.session.get('pid')

            Pdata = Product_mst_table.objects.get(id=uid)

            print ('Successfully searched an item')

            return render (request,'index.html',{'Pdata' : Pdata})
        else :
            print ("Error! search failed")
    
    return render (request,'index.html')

def add (request):

    if request.method == 'POST':

        newuser = ImageForm(request.POST,request.FILES)

        if newuser.is_valid():
            newuser.save()
            print ("Data inserted successfully.")
        else :
            print (newuser.errors)
    
    return render (request,'add.html')

def product (request):

    data = Product_mst_table.objects.all()
    
    return render (request,'product.html',{'data':data})
