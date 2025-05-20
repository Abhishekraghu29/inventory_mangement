from django.urls import path
from .views import *

urlpatterns = [

    path('', login, name='login'),
    path('signup/',register, name='signup'),
    path('forget/',forget, name='forget'),
    path('base/',base, name='base'),
    path('category/',category, name='category'),
    path('system_users/',system_users, name='system_users'),
    path('products/',product, name='product'),
    path('supplier/',supplier, name='supplier'),
    path('sales/',sales, name='sales'),
    path('delete-product/<int:product_id>/',delete_product, name='delete_product'),
    path('delete-supplier/<int:supplier_id>/',delete_supplier, name='delete_supplier'),
    path('delete-sales/<int:sales_id>/',delete_sales, name='delete_sales'),
    path('delete-category/<int:category_id>/',delete_category, name='delete_category'),

    path('product/edit/<int:pk>/',edit_product, name='edit_product'),

    
    # path('users/',user_list, name='user_list'),
]
