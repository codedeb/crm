from django.shortcuts import render, redirect
from .models import Customer, Order, Product
from django.views import generic, View
from django.http import Http404
from django.shortcuts import get_object_or_404
from .forms import OrderForm
from django.urls import reverse



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

def createorder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = OrderForm()
    context = {
        'form' :form,
    }
    return render (request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    form = OrderForm()
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        raise Http404('Order DoesNot Exists')
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    # form=OrderForm()
    context  = {
        'form' : form,
    }
    return render (request, 'accounts/order_form.html', context)

def deleteOrder(request,pk):
    try:
        order = Order.objects.get(id=pk)
    except Order.DoesNotExist:
        raise Http404('Order DoesNot Exists')

    if request.method =='POST':
        order.delete()
        return redirect('/')
    context = {
        'order' :order
    }
    return render(request, 'accounts/delete_form.html', context)

class CreateOrder(generic.CreateView):
    model = Order
    template_name='accounts/order_form.html'
    form_class = OrderForm
    def get_success_url(self):
        return ('/')

class UpdateOrder(generic.UpdateView):
    model = Order
    template_name='accounts/order_form.html'
    form_class = OrderForm
    
    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Order, id=id_)

    def get_success_url(self):
        return ('/')

class DeleteOrder(generic.DeleteView):
    model = Order
    template_name = 'accounts/delete_form.html'

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404(Order, id=id_)

    def get_success_url(self):
        return reverse ('home_view')