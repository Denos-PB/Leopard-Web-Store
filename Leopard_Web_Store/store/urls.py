from django.urls import path
from .views import ProductListView, AddToCartView

urlpatterns = [
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
]
