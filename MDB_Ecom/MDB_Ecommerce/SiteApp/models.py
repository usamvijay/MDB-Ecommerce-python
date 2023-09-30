from django.db import models
from DashboardApp.models import Products

# Create your models here.

class User_data(models.Model):  
   firstname  =      models.CharField(max_length=30)
   lastname   =      models.CharField(max_length=50, null=True)  
   mobile     =      models.CharField(max_length=50, null=True) 
   email      =      models.EmailField( null=True)  
   password   =      models.CharField(max_length=200)
   JoinedAt   =      models.DateField(auto_now=True)

   def __str__(self):
        return self.firstname
   


class Cart(models.Model):
    user       =  models.ForeignKey(User_data, on_delete = models.CASCADE)
    Item       =  models.ForeignKey(Products, on_delete = models.CASCADE)
    color      =  models.CharField(max_length=50)
    size       =  models.CharField(max_length=50)
    qty        =  models.CharField(max_length=50, default=1, null=True)
    price      =  models.IntegerField()
    Added_at   =  models.DateTimeField(auto_now=True)


class OrderAddress(models.Model):
   user         =      models.ForeignKey(User_data, on_delete=models.CASCADE)
   firstname    =      models.CharField(max_length=30)
   lastname     =      models.CharField(max_length=100, null=True)   
   address      =      models.CharField(max_length=500)  
   appartment   =      models.CharField(max_length=100, null=True)  
   city         =      models.CharField(max_length=100)  
   state        =      models.CharField(max_length=10)    
   Zip_code     =      models.IntegerField( )  
   mobile       =      models.CharField(max_length=50)
   email        =      models.EmailField( null=True)  
   created_At   =      models.DateField(auto_now=True)


Orders_Status = (
    (20, "Pending"),
    (40, "Confirmed"),
    (60, "Shipped"),
    (80, "Our for Delevery"),
    (100, "Delevered"),
    (0, "Cancel"),
)
class Orders_items(models.Model):
   user         =      models.ForeignKey(User_data, on_delete=models.CASCADE)
   product      =      models.ForeignKey(Products, on_delete=models.CASCADE)
   address      =      models.ForeignKey(OrderAddress, on_delete=models.CASCADE, null=True)
   price        =      models.IntegerField(null=False)
   Quantity     =      models.IntegerField(null=False)
   color        =      models.CharField(max_length=150, null=True)
   Orders_id    =      models.CharField(max_length=150, null=True)
   created_At   =      models.DateField(auto_now=True)
   order_status  =     models.IntegerField(default=25, choices=Orders_Status)
   

