from django.shortcuts import render
from . models import Customer, Order, Product
# from django.http import HttpResponse


def homeView(request):
    return render(request,"accounts/dashboard.html")

def productView(request):
    obj= Product.objects.all()
    context = {
        'object':obj
    }
    return render(request,"accounts/products.html", context)
    
def customerView(request):
    return render(request,"accounts/customers.html")