from hashlib import md5
import random
from six import ensure_binary
from urllib import request
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from SiteApp.models import User_data, Cart as User_Cart, Orders_items
from SiteApp.models import *
from DashboardApp.models import Categories, Products
# from SiteApp.models import User, User_Cart as add_Cart
from django.contrib import messages
from django.contrib.auth import login, authenticate
from SiteApp import models
from DashboardApp import models

# Create your views here.


def isAlreadyLogin(request):
    if request.session.has_key('User_email') and request.session.has_key('User_role') and request.session.has_key('User_id'):
        return True
    return False


def search_items(request):
    Cat = Categories.objects.all()
    searchName = request.GET.get('search')
    items = Products.objects.filter(Item__icontains=searchName)
    return render(request, 'Site/search_items.html', {'item': items, 'category': Cat})


def index(request):
    Cat = Categories.objects.all()
    Items = Products.objects.all().order_by('-id')[0:18]
    recomended = Products.objects.all().order_by('id')[0:12]

    return render(request, 'Site/index.html', {'category': Cat, 'items': Items, 'Rec': recomended})


def profilePage(request):
    user = User_data.objects.filter(email=request.session['User_email'])

    return render(request, 'Site/profilePage.html', {'User': user})


def User_Register_page(request):
    return render(request, 'Site/User_Register.html')


def login_page(request):
    return render(request, 'Site/Login.html')


def list_view(request):
    filt1 = request.GET.get('min')
    filt2 = request.GET.get('max')
    category = Categories.objects.all()
    CatID = request.GET.get('category')
    if filt1 and filt2:
        items = Products.objects.filter(descount_price__range=(filt1, filt2))
    elif CatID:

        items = Products.objects.filter(Category=CatID)
    else:
        items = Products.objects.all()
    return render(request, 'Site/List_view.html', {'item': items, 'category': category})


def grid_view(request):
    filt1 = request.GET.get('min')
    filt2 = request.GET.get('max')
    category = Categories.objects.all()
    CatID = request.GET.get('category')
    if filt1 and filt2:
        items = Products.objects.filter(descount_price__range=(filt1, filt2))
    elif CatID:

        items = Products.objects.filter(Category=CatID)
    else:
        items = Products.objects.all()
    return render(request, 'Site/Grid_view.html', {'item': items, 'category': category})


def cart_page(request):
    if isAlreadyLogin(request):
        user = request.session['User_email']
        User = User_data.objects.get(email=user)
        User_id = User.id
        Cart_item = User_Cart.objects.filter(user_id=User_id)
        total_price = 0
        for item in Cart_item:
            total_price = total_price + \
                int(item.Item.descount_price) * int(item.qty)
    else:
        messages.info(request, "You have to login first..")
        return HttpResponseRedirect('/Site/User_login')

    return render(request, 'Site/Cart.html', {'cart': Cart_item, 'total': total_price, })


def product_detail_page(request, id):
    item = Products.objects.filter(id=id)
    items = Products.objects.get(id=id)
    SimilarItems = Products.objects.filter(Category=items.id).exclude(id=id)
    return render(request, 'Site/Product_details.html', {'item': item, 'similar': SimilarItems})


def Checkout_page(request):
    if isAlreadyLogin(request):
        User = User_data.objects.get(email=request.session['User_email'])
        address = OrderAddress.objects.filter(user=User.id).order_by('-id')
        User_id = User.id
        Cart_item = User_Cart.objects.filter(user_id=User_id)

        total_price = 0
        for item in Cart_item:
            total_price = total_price + \
                int(item.Item.descount_price) * int(item.qty)
    else:
        messages.info(request, "You have to login first..")
    return render(request, 'Site/Checkout.html', {'address': address, "item": Cart_item, 'total_price': total_price})


def User_Registration_Data(request):
    if request.method == 'POST':
        if User_data.objects.filter(email=request.POST['email']).exists():
            messages.warning(request, "You'r Email is already Registered")
            return HttpResponseRedirect('Site/Register')
        else:
            if request.POST['password'] == request.POST['Cpassword']:
                User = User_data()

                User.firstname = request.POST['firstname']
                User.lastname = request.POST['lastname']
                User.mobile = request.POST['mobile']
                User.email = request.POST['email']
                User.password = md5(ensure_binary(
                    request.POST['password'])).hexdigest()
                User.save()
                messages.warning(
                    request, "You'r Register Succesfully.. Please Login Now .!")
                return redirect('/Site/login_page')
            else:
                messages.warning(request, "Invalide Email Or Password...!")
                return HttpResponseRedirect('/Site/Register')
    else:
        return redirect('/home')


def User_authentication(request):
    if isAlreadyLogin(request):
        return HttpResponseRedirect('/Site/home/')
    elif request.method == 'POST':
        email = request.POST['email']
        password = md5(ensure_binary(request.POST['password'])).hexdigest()
        if User_data.objects.filter(email=email, password=password).exists():
            user = User_data.objects.get(email=email)
            request.session['User_email'] = email
            request.session['User_role'] = 'user'
            request.session['User_id'] = user.id
            messages.success(request, "You are now logged in Succesfully...!")
            return HttpResponseRedirect('/Site/home/')
        else:
            messages.info(request, "Invalid Email or Password")
            return redirect('/Site/login_page/')
    else:
        return redirect('/Site/login_page/')


def User_logout(request):
    if isAlreadyLogin(request):
        try:
            del request.session['User_email']
            del request.session['User_role']
        except:
            pass
        messages.info(request, "You're Loged out Now.....")
        return HttpResponseRedirect('/Site/home')


def add_items_to_cart(request):
    if isAlreadyLogin(request):
        if request.method == 'POST':
            user = User_data.objects.get(email=request.session['User_email'])
            UserId = user.id
            if User_Cart.objects.filter(Item=request.POST['item'], user=UserId).exists():
                messages.info(request, 'Item is alredy in Cart')
                return redirect('/Site/cart_page')
            else:
                user_id = UserId
                qty = request.POST['qty']
                Cart = User_Cart()
                Cart.user_id = user_id
                Cart.Item_id = request.POST['item']
                Cart.size = request.POST['size']
                Cart.qty = request.POST['qty']
                Cart.color = request.POST['color']
                cart_total_price = 0
                price = request.POST['price']
                total_cart = cart_total_price + int(price) * int(qty)
                Cart.price = total_cart
                Cart.save()
                messages.success(request, "Item Added To Cart Successfully")
                return HttpResponseRedirect('/Site/cart_page')

        else:
            return HttpResponseRedirect('/Site/cart_page')
    else:
        return HttpResponseRedirect('/Site/login_page')


def UpdateCart(request):
    if isAlreadyLogin(request):
        if request.method == 'POST':
            qty = request.POST['qty']
            CartId = request.POST['cartid']
            Cart = User_Cart.objects.get(id=CartId)
            Cart.qty = qty
            cart_total_price = 0
            price = request.POST['price']
            total_cart = cart_total_price + int(price) * int(qty)
            Cart.price = total_cart
            Cart.save()
            messages.info(request, "Wow... You're Updated Cart")
            return HttpResponseRedirect('/Site/cart_page')
        else:
            return HttpResponseRedirect('/Site/cart_page')

    else:
        return HttpResponseRedirect('/Site/login_page')


def Remove_cart_item(request, id):
    cart_item = User_Cart.objects.get(id=id)
    cart_item.delete()
    messages.success(request, "Cart Item deleted  Successfully")
    return HttpResponseRedirect('/Site/cart_page')


def Orderview(request):
    return render(request, 'Site/OrderView.html')


def AddDeleveryAddress(request):
    if isAlreadyLogin(request):
        if request.method == "POST":
            User = User_data.objects.get(email=request.session['User_email'])
            User = User.id
            address = OrderAddress()
            address.user_id = User
            address.firstname = request.POST['firstname']
            address.lastname = request.POST['lastname']
            address.address = request.POST['address']
            address.appartment = request.POST['house']
            address.city = request.POST['city']
            address.state = request.POST['state']
            address.Zip_code = request.POST['zipcode']
            address.mobile = request.POST['mobile']
            address.email = request.POST['email']
            Orders_id = 'VIMDB'+str(random.randint(111111, 9999999999999))
            while OrderAddress.objects.filter(Orders_id=Orders_id) is None:
                Orders_id = 'PV'+str(random.randint(111111, 9999999999999))
            address.tracing_number = Orders_id
            address.save()
        messages.info(request, "Order Succuss...")
        return HttpResponseRedirect('/Site/home')
    else:
        return HttpResponseRedirect('/Site/login_page')


def ProccedToCheckout(request):
    if isAlreadyLogin(request):
        if request.method == "POST":
            User = User_data.objects.get(email=request.session['User_email'])
            User = User.id
            address = request.POST['address']
            Orders_id = 'VIMDB'+str(random.randint(111111, 9999999999999))
            while Orders_items.objects.filter(Orders_id=Orders_id) is None:
                Orders_id = 'PV'+str(random.randint(111111, 9999999999999))
            Cart = User_Cart.objects.filter(user=User)
            for item in Cart:
                Orders_items.objects.create(
                    user_id=User,
                    product=item.Item,
                    price=item.Item.descount_price,
                    Quantity=item.qty,
                    color=item.color,
                    address_id=address,
                    Orders_id=Orders_id
                )
                items = Products.objects.filter(id=item.Item_id).first()
                items.Qty = int(items.Qty) - int(item.qty)
                items.save()
                User_Cart.objects.filter(user=User).delete()
                messages.info(request, "Order Succuss...")
        else:
            return HttpResponseRedirect('/Site/Checkout_page')
    else:
        return HttpResponseRedirect('/Site/login_page')
    return HttpResponseRedirect('/Site/MyOrdersPage')


def MyOrdersPage(request):
    user = User_data.objects.get(email=request.session['User_email'])
    orders = Orders_items.objects.filter(user=user.id).order_by('-id')
    return render(request, 'Site/MyOrders.html', {'Order': orders, })


def TrackOrder(request, id):
    user = User_data.objects.filter(email=request.session['User_email'])
    orders = Orders_items.objects.filter(id=id)

    return render(request, 'Site/TrackOrder.html', {'Order': orders, 'User': user})


def UpdateUserProfile(request, id ):
    if request.method == 'POST':
        User = User_data.objects.get(id = id)
        
        User.firstname = request.POST['firstname']
        User.lastname = request.POST['lastname']
        User.mobile = request.POST['mobile']
        User.email = request.POST['email']
        User.save()
        messages.warning(
            request, "You'r Profile is Updated Succesfully...!")
        return redirect('/Site/profilePage')
    else:
         user = User_data.objects.filter(id = id)
         return render(request, 'Site/UpdateProfile.html', {'User': user })

def updatePassword(request):
    return render(request, 'Site/updatePassword.html')


def changepassword(request):
    if isAlreadyLogin(request):
        oldpass = md5(ensure_binary(request.POST['Oldpass'])).hexdigest()
        newpass =  md5(ensure_binary (request.POST['pass'])).hexdigest()
        if request.method =='POST':
            if User_data.objects.filter(email = request.session['User_email'], password = oldpass):
                if request.POST['pass'] == request.POST['Cpass']:
                    User = User_data.objects.filter(email = request.session['User_email'])
                    for i in User :
                        i.password = newpass
                        i.save()
                    messages.info(request,'Changed Your Password  Succesfully..')
                    return HttpResponseRedirect('/Site/profilePage')
                else:
                    messages.info(request,'New password and Confirm password Must Be Same..')
                    return HttpResponseRedirect('/Site/updatePassword')
            else:
                messages.info(request,'Email or Old password is incorrect...')
                return HttpResponseRedirect('/Site/updatePassword')
        else:
            return HttpResponseRedirect('/Site/profilePage')
    return render(request, '/Site/updatePassword.html')