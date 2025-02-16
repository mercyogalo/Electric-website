from django.shortcuts import render, redirect
from django.contrib import messages
from cart.cart import Cart
from .forms import ShippingForm, UserInfoForm
from .models import ShippingAddress
from django.contrib.auth.models import User

def shipping(request):
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.get_quants

    # Ensure shipping_form is always initialized
    shipping_form = None  

    if request.user.is_authenticated:
        current_user = request.user
        shipping_user = ShippingAddress.objects.filter(user=current_user).first()  # Prevent DoesNotExist error

        # Get user form
        form = UserInfoForm(request.POST or None, instance=current_user)
        # Get shipping form
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)

        if form.is_valid() and shipping_form.is_valid():
            form.save()
            shipping_form.save()
            messages.success(request, "Your Info Has Been Updated!!")
            return redirect('home')
    else:
        messages.error(request, "You Must Be Logged In To Access That Page!!")
        return redirect('login')  # Redirect to login instead of rendering the page

    context = {
        'cart_products': cart_products,
        'quantities': quantities,
        'shipping_form': shipping_form,
    }

    return render(request, 'shop_features/shipping.html', context)
