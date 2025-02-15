from django.shortcuts import render,get_object_or_404,redirect
from . cart import Cart
from shop_features.models import Product
from django.http import JsonResponse
from django.contrib import messages
# Create your views here.

def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prods()
    quantities=cart.get_quants()
    totals=cart.total()
    context={
       'cart_products':cart_products,
       'quantities':quantities,
       'totals':totals,
    }
    return render(request,'shop_features/cart_summary.html', context)

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product=get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=product_qty)
        
        cart_quantity= cart.__len__()
        response = JsonResponse({'qty': cart_quantity})
    
        return response
    return JsonResponse({"error": "Invalid request method"}, status=400)

def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        
        product = get_object_or_404(Product, id=product_id)
        cart.update(product=product, quantity=product_qty)
        messages.success(request, ("Your Cart Has Been Updated..."))
        return redirect('cart:cart_summary')
    
    return redirect('cart:cart_summary')



    

def cart_delete(request):
    cart = Cart(request)
    
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)
        
        response = JsonResponse({'product': product_id})
    
        return response
        
               
    