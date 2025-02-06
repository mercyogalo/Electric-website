from django.shortcuts import render, redirect, get_object_or_404
from . models import Product, Category
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . forms import SignUpForm
from . shop_features import Cart
from django.http import JsonResponse

# Create your views here.

def home(request):
    products=Product.objects.all()
    items=Category.objects.all()
    context={
        "products": products,
        "items":items,
    }
    return render(request,'index.html', context)

def store(request):
    items=Product.objects.all()
    context={
        "items":items,
    }
    return render(request,'store.html', context)


def shipping(request):
    cart=Cart(request)
    cart_products=cart.get_prods
    quantities=cart.get_quants
    context={
       'cart_products':cart_products,
       'quantities':quantities,
    }
    return render(request,'shipping.html',context)


def laptop(request):
    return render(request,'laptop.html')


def login_user(request):
    context={
        "messages": messages
    }
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,("Logged in sucessfully"))
            return redirect ('shop_features:home')
        else:
            messages.error(request,("There was an error please try again..."))
            return redirect('shop_features:login')
    else:
        return render(request,'login.html',context)
    

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out successfully"))
    return redirect('shop_features:home')


def register_user(request):
    form=SignUpForm()
    context={
        "form": form,
        "messages": messages
    }
    if request.method=="POST":
        form=SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            
            #login user
            user=authenticate(request, username=username, password=password)
            login(request,user)
            messages.success(request, ("You have created an account  successfully"))
            return redirect('shop_features:home')
        else:
            messages.error(request, ("Their was a problem with your registration. Kindly try again."))
            return redirect('shop_features:register')
    else:   
         return render(request,'register.html',context)
     
     
def product(request,pk):
    product=Product.objects.get(id=pk)
    items=Product.objects.all()
    context={
        "product": product,
        "items":items,
    }
    return render(request,'product.html',context)


def cart_summary(request):
    cart=Cart(request)
    cart_products=cart.get_prods
    quantities=cart.get_quants
    context={
       'cart_products':cart_products,
       'quantities':quantities,
    }
    return render(request,'cart_summary.html', context)

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
        
        cart.update(product=product_id,quantity=product_qty)
        
        return redirect('shop_features:cart_summary')
    
    
    
    messages.success(request, ("Your Cart Has Been Updated..."))
    return messages



    

def cart_delete(request):
    cart = Cart(request)
    
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        
        cart.delete(product=product_id)
        
        response = JsonResponse({'product': product_id})
    
        return response
        
        
    