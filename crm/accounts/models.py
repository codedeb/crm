from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length = 20, null = True)
    phone = models.IntegerField(null = True)
    email = models.CharField(max_length = 50, null = True)
    date_created = models.DateTimeField(auto_now_add = True)

class Tag(models.Model):
    name = models.CharField(max_length=20, null=True)

class Product(models.Model):
    PRODUCT_CATEGORY = [
        ('outdoor', 'outdoor'),
        ('indoor', 'indoor')
    ]
    name = models.CharField(max_length=30, null= True)
    price = models.IntegerField(null = True)   
    category = models.CharField(max_length = 50,null = True, choices = PRODUCT_CATEGORY)
    description = models.TextField(null =True)
    date_created = models.DateTimeField(auto_now_add = True)
    tag = models.ManyToManyField(Tag)

class Order(models.Model):
    ORDER_STATUS = [
        ('delivered', 'delivered'),
        ('pending', 'pending'),
        ('out-for-delivery', 'out-for-delivery')
    ]
    customer = models.ForeignKey(Customer, null=True, on_delete =models.SET_NULL)
    product = models.ForeignKey(Product, null = True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add = True)
    status = models.CharField(max_length = 20, choices = ORDER_STATUS)