from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress


def shipping(request):
    context = {}
    return render(request, 'shop_features/shipping.html', context)
