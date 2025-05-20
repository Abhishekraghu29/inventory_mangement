from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.contrib.auth.models import product
from .models import signup
from .models import Product
from .models import Suppliers
from .models import Sales
from .models import Category
class SignUpForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    class Meta:
        model =signup
        fields = ('username', 'password','password2')

class System_user(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1','password2')

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['id','name', 'category', 'supplier', 'price']

class SupplierForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = ['id','name' ,'proname',  'contact']
       
            



        


class SalesForm(forms.ModelForm):
    class Meta:
        model = Sales
        fields = ['id','name', 'cp', 'sp', 'quantity']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['id', 'name', 'stock', 'PurchesList']