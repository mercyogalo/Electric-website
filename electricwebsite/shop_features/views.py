from django.shortcuts import render, redirect
from . models import Product
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from . forms import SignUpForm
# Create your views here.

def home(request):
    products=Product.objects.all()
    context={
        "products": products,
    }
    return render(request,'index.html', context)

def store(request):
    return render(request,'store.html')

def product(request):
    return render(request,'product.html')

def checkout(request):
    return render(request,'checkout.html')


def laptop(request):
    return render(request,'laptop.html')


def login_user(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user= authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request,("Logged in sucessfully"))
            return redirect ('shop_features:home')
        else:
            messages.success(request,("There was an error please try again..."))
            return redirect('shop_features:login')
    else:
        return render(request,'login.html')
    

def logout_user(request):
    logout(request)
    messages.success(request, ("You have been logged out successfully"))
    return redirect('shop_features:home')


def register_user(request):
    form=SignUpForm
    return render(request,'register.html')