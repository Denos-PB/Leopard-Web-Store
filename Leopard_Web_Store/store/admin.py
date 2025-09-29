from django.contrib import admin
from django.utils.html import format_html
from django.db import models
from .models import Product, Category, Cart, CartItem

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'gender', 'size', 'category', 'image_preview')
    list_filter = ('gender', 'size', 'category__name')
    search_fields = ('name', 'description')
    fields = ('name', 'price', 'image', 'gender', 'size', 'description', 'category')
    list_editable = ('price', 'size')
    list_per_page = 25
    autocomplete_fields = ('category',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_items_count', 'get_total_price', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('user__username',)

    def get_items_count(self, obj):
        return obj.items.count()
    get_items_count.short_description = 'Кількість товарів'

    def get_total_price(self, obj):
        total = sum(item.product.price * item.quantity for item in obj.cartitem_set.all())
        return f"{total:.2f} грн"
    get_total_price.short_description = 'Загальна сума'

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('product__gender', 'product__size')
    search_fields = ('product__name',)
    autocomplete_fields = ('product',)