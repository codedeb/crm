from django.shortcuts import render
from . models import Customer, Order, Product
from django.views import generic, View
from django.http import Http404
from django.shortcuts import get_object_or_404


def homeView(request):
    return render(request,"accounts/dashboard.html")

class HomeView(View):
    def get(self, request,*args, **kwargs):
        customers = Customer.objects.all()
        orders = Order.objects.all()
        ordersCount = orders.count()
        customerCount = customers.count()
        orderDelivered = Order.objects.filter(status='delivered').count()
        orderPending = Order.objects.filter(status='pending').count()
        context = {
            'customers' : customers,
            'orders' : orders,
            'ordersCount' : ordersCount,
            'orderDelivered': orderDelivered,
            'orderPending': orderPending,
        }
        return render(request,"accounts/dashboard.html", context)


class ProductView(generic.ListView):
    model = Product
    # queryset = Product.objects.all()
    template_name = "accounts/products.html"
    context_object_name= 'products'

def productView(request):
    obj= Product.objects.all()
    context = {
        'object':obj
    }
    return render(request,"accounts/products.html", context)
    
def customerView(request):
    return render(request,"accounts/customers.html")

def customerview(request, pk): 
    try:
        customer = Customer.objects.get(id=pk)
    except Customer.DoesNotExist:
        raise Http404('Page DoesNot Exists')
    orders = customer.order_set.all()
    ordercount = orders.count()
    context = {
        'customer' : customer,
        'order' : order,
        'ordercount':ordercount,
    }   
    return render(request, 'accounts/customers.html', context)

class CustomerView(generic.DetailView):
    model=Customer
    template_name = 'accounts/customers.html'
    # context_object_name = 'orders'

    def get_object(self, ** kwargs):
        get_id = self.kwargs.get('pk')
        customer = get_object_or_404(Customer, pk=get_id)
        return customer
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        get_id = self.kwargs.get('pk')
        customer = get_object_or_404(Customer, pk=get_id)
        orders = customer.order_set.all()
        ordercount = orders.count()
        context['orders'] = orders
        context['ordercount'] = ordercount
        return context
