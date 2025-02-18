from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart
from .forms import ShippingForm
from .models import ShippingAddress
from django.contrib.auth.decorators import login_required  

@login_required  
def shipping(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants


    shipping_user = ShippingAddress.objects.filter(user=request.user).first()


    shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

    if request.method == "POST" and shipping_form.is_valid():
        shipping_form.save()
        messages.success(request, "Your Shipping Information Has Been Updated!")
        return redirect('home')

    context = {
        'cart_products': cart_products,
        'quantities': quantities,
        'shipping_form': shipping_form,
    }

    return render(request, 'shop_features/shipping.html', context)
