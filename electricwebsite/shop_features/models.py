from django.db import models

# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    
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
    
    
class Order(models.Model):






class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.IntegerField()
    category=models.CharField(max_length=100)
    description=models.CharField( max_length=50)
    image=models.ImageField( upload_to='productimage/')
    

    def __str__(name):
        return 

    
