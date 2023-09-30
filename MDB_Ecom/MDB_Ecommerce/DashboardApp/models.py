from django.db import models

# Create your models here.

class Categories(models.Model):
    Category_name  =  models.CharField(max_length= 50)
    Category_icon  =  models.ImageField(default="null", upload_to= 'media/Categories/')
    slug           =  models.SlugField(default= "", null=False)
    Addet_at       =  models.DateField(auto_now_add=True)

class Products(models.Model):
    Category              =       models.ForeignKey(Categories, on_delete= models.CASCADE,)
    Item                  =       models.CharField(max_length= 50)
    Item_image            =       models.ImageField(default="null",  upload_to='media/Products/' )
    Total_price           =       models.IntegerField()
    descount_price        =       models.IntegerField()
    Qty                   =       models.IntegerField()
    Description           =       models.CharField(max_length=2000)
    slug                  =       models.SlugField(default= "", null=False)
    Created_At            =       models.DateField(auto_now  = True)