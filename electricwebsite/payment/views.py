from django.shortcuts import render, redirect, get_object_or_404
from shop_features.models import Product
from django.contrib import messages
from cart.cart import Cart
from django.http import JsonResponse

# Create your views here.

# Create your views here.
def shipping(request):
    cart=Cart(request)
    cart_products=cart.get_prods
    quantities=cart.get_quants
    context={
       'cart_products':cart_products,
       'quantities':quantities,
    }
    return render(request,'shop_features/shipping.html',context)

