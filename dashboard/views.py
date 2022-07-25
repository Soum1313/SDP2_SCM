from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Product,Order
from .forms import ProductForm,OrderForm
from django.contrib.auth.models import User
from django.contrib import messages

import pymongo
connect_string='mongodb+srv://admin:admin123@scm.ggsve.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
from django.conf import settings
my_client = pymongo.MongoClient(connect_string)
dbname=my_client['SDP-2']
collection_name=dbname["dashboard_product"]
# Create your views here.
@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    products_count=Product.objects.all().count()
    
    workers_count=User.objects.all().count()
    orders_count=Order.objects.all().count()
    if request.method=='POST':
        form=OrderForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.customer=request.user
            instance.save()
            return redirect('dashboard-index')
    else:
        form = OrderForm()
    context ={
        'orders':orders,
        'form':form,
        'products':products,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request, 'dashboard/index.htm',context)

@login_required
def home(request):
    # print(request.user)
    # if request.user.is_anonymous:
    #     return redirect("/login") 
    return render(request, 'dashboard/home.htm')

@login_required
def contact(request):
    # print(request.user)
    # if request.user.is_anonymous:
    #     return redirect("/login") 
    return render(request, 'dashboard/contact.htm')

@login_required
def about(request):
    # print(request.user)
    # if request.user.is_anonymous:
    #     return redirect("/login") 
    return render(request, 'dashboard/about.htm')


@login_required
def staff(request):
    workers = User.objects.all()
    workers_count=workers.count()
    orders_count=Order.objects.all().count()
    products_count=Product.objects.all().count()
    context ={
        'workers':workers,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count
    }
    return render(request, 'dashboard/staff.htm',context)

@login_required
def staff_detail(request,pk):
    workers = User.objects.get(id=pk)
   
    context ={
        'workers':workers,
        

    }
    return render(request,'dashboard/staffDetail.htm',context)


@login_required
def  product(request):
    #items=Product.objects.all()

    # items = Product.objects.raw('SELECT * FROM dashboard_product')
    items= collection_name.find({})
    products_count=Product.objects.all().count()
    
    workers_count=User.objects.all().count()
    orders_count=Order.objects.all().count()
    if request.method == 'POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name=form.cleaned_data.get('name')
            messages.success(request,f'{product_name} has been added' )
            return redirect('dashboard-product')
    else:
        form=ProductForm()
    

    context={
        'items':items,
        'form':form,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count
    }
    return render(request, 'dashboard/product.htm',context)

@login_required
def productDelete(request,pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    return render(request,'dashboard/productDelete.htm')

@login_required
def product_update(request , pk):
    item = Product.objects.get(id=pk)
    if request.method=='POST':
            form = ProductForm(request.POST,instance=item)
            if form.is_valid():
                form.save()
                return redirect('dashboard-product')
    else :
        form = ProductForm(instance=item)        
    context={
        'form':form,
    }
    return render(request , 'dashboard/productUpdate.htm',context)

@login_required
def order(request):
    orders = Order.objects.all()
    orders_count=orders.count()
    workers_count=User.objects.all().count()
    products_count=Product.objects.all().count()
    context={
        'orders':orders,
        'workers_count':workers_count,
        'orders_count':orders_count,
        'products_count':products_count,
    }
    return render(request, 'dashboard/order.htm',context)