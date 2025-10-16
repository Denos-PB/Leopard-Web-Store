from django.urls import path
from .views import RegisterView, LoginView, AdminOnlyView, ModeratorView, CartView
from .views import ProductListView, AddToCartView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('products/', ProductListView.as_view(), name='product-list'),
    path('cart/', CartView.as_view(), name='cart-view'),
    path('cart/add/', AddToCartView.as_view(), name='add-to-cart'),
    path('admin-only/', AdminOnlyView.as_view(), name='admin-only'),
    path('moderator/', ModeratorView.as_view(), name='moderator'),
]
