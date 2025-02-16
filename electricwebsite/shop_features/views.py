from django.shortcuts import render, redirect, get_object_or_404
from . models import Product, Category
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from cart.cart import Cart
from . forms import SignUpForm
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


def contact(request):
    if request.method=="POST":
        first_name=request.POST['first-name']
        last_name=request.POST['last-name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        
        
        messages.success(request, ("You message has been received succcessfully. Our team will reach out shortly."))
        return messages
    
    return render(request,'contact.html')

def order(request):
    pass
