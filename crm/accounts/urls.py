from django.urls import path, include
from . views import homeView, productView, customerView

urlpatterns = [
    path("", homeView, name="home_view"),
    path("products/", productView, name="product_view"),
    path("customers/", customerView, name="customer_view")
    ]

