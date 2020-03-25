from django.urls import path, include
from . views import CustomerView, ProductView, HomeView

urlpatterns = [
    path("", HomeView.as_view(), name="home_view"),
    path("products/", ProductView.as_view(), name="product_view"),
    path("customers/<pk>/", CustomerView.as_view(), name="customer_view"),
    # path("customers/<pk>/", CustomerDetailView.as_view(), name = 'customer_detail'),
    ]

