from django.db import models

# Create your models here.

class signup(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=100 )
    password = models.CharField(max_length=100)
    password2 = models.CharField(max_length=100)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100, default=None)
    supplier = models.CharField(max_length=100, default=None)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
  

class Suppliers(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    proname = models.CharField(max_length=100, default=None)
    contact = models.CharField(max_length=15)

class Sales(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    cp = models.CharField(max_length=100, default=None)
    sp = models.CharField(max_length=100, default=None)
    quantity = models.CharField(max_length=15)

class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    stock = models.CharField(max_length=100, default=None)
    PurchesList = models.CharField(max_length=100, default=None)
    

