from django import views
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from DashboardApp import urls
from DashboardApp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashbaord/', views.Dashbaord),
    path('Categories/', views.categories_list),
    path('Adding_Categories/', views.Adding_Categories),
    path('products/', views.products),
    path('add_products/', views.adding_products),
    path('product_list/', views.product_list),
    path('UserOrders/', views.UserOrders),
    path('RemoveProduct/<int:id>', views.RemoveProduct),
    path('DeleteCategory/<int:id>', views.DeleteCategory),
  

]