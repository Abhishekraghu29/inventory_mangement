

# Register your models here.

from django.contrib import admin
from .models import signup,Product,Suppliers,Sales,Category


@admin.register(signup)
class SignupAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'username','password', 'password2')

@admin.register(Product)
class productAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'category', 'supplier', 'price')
    
@admin.register(Suppliers)
class supplierAdmin(admin.ModelAdmin):
    list_display = ('id','name','proname', 'contact')

@admin.register(Sales)
class salesAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'cp', 'sp', 'quantity')

@admin.register(Category)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'stock', 'PurchesList')