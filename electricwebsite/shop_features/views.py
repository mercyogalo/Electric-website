from django.shortcuts import render, redirect, get_object_or_404
from . models import Product
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . forms import SignUpForm
from . cart import Cart
from django.http import JsonResponse

# Create your views here.

def home(request):
    products=Product.objects.all()
    context={
        "products": products,
    }
    return render(request,'index.html', context)

def store(request):
    return render(request,'store.html')


def checkout(request):
    return render(request,'checkout.html')


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
    context={
        
    }
    return render(request,'cart_summary.html', context)

def cart_add(request):
    cart = Cart(request)
    
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product=get_object_or_404(Product, id=product.id)
        cart.add(product=product)
        
        
        response = JsonResponse({'Product Name: ': product.name})
        
    
        return response


def cart_update(request):
    pass

def cart_delete(request):
    pass