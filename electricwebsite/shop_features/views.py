from django.shortcuts import render
from . models import Product
# Create your views here.

def home(request):
    context={
        "Product": Product,
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