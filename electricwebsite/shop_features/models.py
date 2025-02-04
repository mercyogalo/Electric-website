from django.db import models
import datetime

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='categoryimage/' , default='default.jpg')
    
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    first_name=models.CharField( max_length=50)
    last_name=models.CharField( max_length=50)
    phone=models.CharField( max_length=50)
    email=models.EmailField()
    password=models.CharField( max_length=50)
    
    
    def __str__(self):
        return  {self.first_name}+{self.last_name}
    
    
    
    
    
class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description=models.CharField( max_length=250, default="", blank=True, null=True)
    image=models.ImageField(upload_to='productimage/' , default='default.jpg')
    is_sale=models.BooleanField(default=False)
    sale_price=models.IntegerField(default=0)
    

    def __str__(self):
        return self.name    
    
class Order(models.Model):
    product=models.ForeignKey(Product, on_delete=models.CASCADE )
    Customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    address=models.CharField( max_length=100, default="", blank=True)
    phone=models.CharField(max_length=100, default="", blank=True, null=True)
    status=models.BooleanField(default="false")
    date=models.DateField(default=datetime.datetime.today)
    
    
    def __str__(self):
        return self.product
    








    
