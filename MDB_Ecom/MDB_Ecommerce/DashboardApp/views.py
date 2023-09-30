from typing import Self
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from django.shortcuts import render
from SiteApp.models import Products, User_data
from SiteApp.models import *
from datetime import datetime

from DashboardApp import models
from .models import Categories

# Create your views here.
def Dashbaord(request):
    items = Products.objects.all()[0:5]
    i = items.count()
    users = User_data.objects.all().count()
    order = Orders_items.objects.all().count()
    cart = Cart.objects.all().count()
    Orders = Orders_items.objects.all()
    
    total_price =0
    for Order in Orders:
        total_price = total_price + int(Order.product.descount_price) * int(Order.Quantity)
    return render(request, 'Dashboard/index.html',{'items': items, 'users': users, 'i': i,"order":order, 'cart':cart, 'total_price':total_price })

def categories_list(request):
    Cat = Categories.objects.all().order_by('-id')
    return render(request, 'Dashboard/Categories.html', { 'Category': Cat })

def Adding_Categories(request):
    if request.method == 'POST':
        Cat =request.POST['Category_name']
        if models.Categories.objects.filter(Category_name = Cat).exists():
            messages.warning(request, "This Categories is already added..!")
            return HttpResponseRedirect('/Categories')
        else:
            Category = models.Categories()
            Category.Category_name = Cat
            Category.Category_icon = request.FILES['image']
            Category.save()
            messages.success(request, "Categories added Succesfully..!")
            return HttpResponseRedirect('/Categories')
    else:
        return HttpResponseRedirect('/Categories')


def products(request):
    category = Categories.objects.all()
    return render(request, 'Dashboard/add_products.html',{'category': category})


def adding_products(request):
    if request.method == 'POST':
        product  = models.Products()
        product.Category_id     = request.POST['cat_id']
        product.Item            = request.POST['item_name']
        product.Item_image      = request.FILES['image']
        product.Total_price     = request.POST['total_price']
        product.descount_price  = request.POST['disc_price']
        product.Qty             = request.POST['Qty']
        product.Description     = request.POST['Description']
        product.save()
        messages.success(request, "Product added Successfully..!")
        return HttpResponseRedirect('/products')
    else:
        return HttpResponseRedirect('/products')


def product_list(request):
    items = Products.objects.all()
    return render(request, 'Dashboard/Products_list.html', {'items':items })

def UserOrders(request):
    Orders  = Orders_items.objects.all().order_by('-id')
    return render(request, 'Dashboard/UserOrders.html',{'Orders':Orders})


def RemoveProduct(request, id):
    items = Products.objects.get(id = id )
    items.delete()
    return HttpResponseRedirect('/product_list')


def DeleteCategory(request, id):
    items = Categories.objects.get(id = id )
    items.delete()
    return HttpResponseRedirect('/Categories')