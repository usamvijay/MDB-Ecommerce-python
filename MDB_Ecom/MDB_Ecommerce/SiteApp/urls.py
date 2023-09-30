from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from SiteApp import urls
from SiteApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index),
    path('Register/', views.User_Register_page),
    path('login_page/', views.login_page),
    path('profilePage/', views.profilePage),
    path('cart_page/', views.cart_page),
    path('list_view/', views.list_view),
    path('search_items/', views.search_items),
    path('Remove_cart_item/<int:id>/', views.Remove_cart_item),
    path('grid_view/', views.grid_view),
    path('product_detail_page/', views.product_detail_page),
    path('product_detail_page/<int:id>/', views.product_detail_page),
    path('Checkout_page/', views.Checkout_page),
    path('User_Registration_form/', views.User_Registration_Data),
    path('User_logout/', views.User_logout),
    path('User_login/', views.User_authentication),
    path('add_items_to_cart/', views.add_items_to_cart),
    path('Orderview/', views.Orderview),
    path('AddDeleveryAddress/', views.AddDeleveryAddress),
    path('ProccedToCheckout/', views.ProccedToCheckout),
    path('TrackOrder/', views.TrackOrder),
    path('TrackOrder/<int:id>/', views.TrackOrder),
    path('MyOrdersPage/', views.MyOrdersPage),
    path('UpdateCart/', views.UpdateCart),
    path('UpdateUserProfile/<int:id>/', views.UpdateUserProfile),
    path('updatePassword/', views.updatePassword),
    path('changepassword/', views.changepassword),

]
