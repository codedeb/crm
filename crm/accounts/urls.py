from django.urls import path, include
from . views import CustomerView, ProductView, HomeView, CreateOrder,UpdateOrder,deleteOrder

urlpatterns = [
    path("", HomeView.as_view(), name="home_view"),
    path("products/", ProductView.as_view(), name="product_view"),
    path("customers/<pk>/", CustomerView.as_view(), name="customer_view"),
    path("create/", CreateOrder.as_view(), name = 'create_order'),
    path("update/<pk>/", UpdateOrder.as_view(), name = 'update_order'),
    path("delete/<pk>/", deleteOrder, name = 'delete_order'),
    ]

