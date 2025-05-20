from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.views import View
from .models import Product
from .models import Suppliers
from .models import Sales
from .models import Category
from django.views.decorators.csrf import csrf_protect
from .forms import ProductForm
from .forms import SupplierForm
from .forms import SalesForm
from .forms import CategoryForm
from.forms import System_user

@csrf_protect
def product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product')  # Replace with your actual redirect
    else:
        form = ProductForm()
        
    # Fetch all products to display in the template
    product = Product.objects.all()

    return render(request, 'product.html',{'form': form ,'products': product})

def delete_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product.delete()
    return redirect('product')

def supplier(request):
    if request.method == 'POST':

        form= SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('supplier')  # Replace with your actual redirect
    else:
        form = SupplierForm()
        
    # Fetch all products to display in the template
    supplier = Suppliers.objects.all()

    return render(request, 'supplier.html',{'form': form ,'suppliers': supplier})

def delete_supplier(request, supplier_id):
    supplier = get_object_or_404(Suppliers, id=supplier_id)
    supplier.delete()
    return redirect('supplier')


def sales(request):
    if request.method == 'POST':
        form2= SalesForm(request.POST)
        if form2.is_valid():
            form2.save()
            return redirect('sales')  # Replace with your actual redirect
    else:
        form2 = SalesForm()
        
    # Fetch all products to display in the template
    products = Sales.objects.all()

    return render(request, 'sales.html',{'form': form2 ,'products': products})

def delete_sales(request, sales_id):
    sales = get_object_or_404(Sales, id=sales_id)
    sales.delete()
    return redirect('sales')


def category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('category')  # Replace with your actual redirect
    else:
        form = CategoryForm()
        
    # Fetch all products to display in the template
    products = Category.objects.all()

    return render(request, 'category.html',{'form': form ,'products': products})

def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    category.delete()
    return redirect('category')






def edit_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product')  # Change to your product page name
    else:
        form = ProductForm(instance=product)

    return render(request, 'edit_product.html', {'form': form, 'product': product})

























def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
         
            return redirect('login')  # Redirect after signup
    else:
        initial_data = {'username': '','password1': '', 'password2': ''}
        form=UserCreationForm(initial= initial_data)

    return render(request, 'signup.html', {'form': form})


def login(request):
     if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        
        if user is not None:
                auth.login(request, user)
                
                return redirect('base')  # or any page you want after login
    
     return render(request, 'login.html')



def forget(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # (Here you can add password reset logic later)
        return redirect('login')  # After password reset, redirect to login page
    return render(request, 'forget.html')   

def base(request):
    data = {
        'system_users': 2,
        'categories': 4,
        'products': 6,
        'suppliers': 2,
        'total_purchases': 3
    }
    return render(request, 'base.html', data)

def category(request):
    return render(request, 'category.html')



def supplier(request):
    return render(request, 'supplier.html')

def sales(request):
    return render(request, 'sales.html')

def system_users(request):
    users = User.objects.all()
    return render(request, 'user_list.html', {'users': users})
    # if request.method == 'POST':
    #     form = System_user(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('system_users')
    # else:
    #     form = System_user()

    # users = User.objects.all()
    # return render(request, 'system_users.html', {'form': form, 'users': users})

# def signup(request):
#     if request.method == 'POST':
#         form = RegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('login')  # After signup, redirect to login page
#     else:
#         form = RegistrationForm()
#     return render(request, 'signup.html', {'form': form})


        


# def user_list(request):
#     # For static list (without database):
#     users = [
#         {'name': 'User 1', 'email': 'user1@example.com'},
#         {'name': 'User 2', 'email': 'user2@example.com'},
#         {'name': 'User 3', 'email': 'user3@example.com'},
#         {'name': 'User 4', 'email': 'user4@example.com'},
#         {'name': 'User 5', 'email': 'user5@example.com'},
#     ]

#     # OR use database:
#     # users = CustomUser.objects.all()[:5]

#     return render(request, 'user_list.html', {'users': users})


