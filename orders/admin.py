from django.contrib import admin
from orders.models import Order, OrderItem


class OrderTabulareAdmin(admin.TabularInline):
    model = Order
    fields = ['requires_delivery', 'delivery_address', 'payment_on_get', 'is_paid', 'created_timestamp']
    search_fields = ['product', 'name']
    readonly_fields = ['created_timestamp']
    extra = 0


class OrderItemTabulareAdmin(admin.TabularInline):
    model = OrderItem
    fields = ['product', 'name', 'price', 'quantity']
    search_fields = ['product', 'name']
    readonly_fields = ['sale_date']
    extra = 0


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'user', 
        'id', 
        'status', 
        'requires_delivery', 
        'delivery_address', 
        'payment_on_get', 
        'is_paid', 
        'created_timestamp'
        ]
    search_fields = ['id']
    readonly_fields = ['id', 'created_timestamp']
    list_filter = ['requires_delivery', 'status', 'payment_on_get', 'is_paid', 'created_timestamp']
    inlines = (OrderItemTabulareAdmin,)
    
    
@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'product', 
        'price',
        'quantity',
        'sale_date'
        ]
    search_fields = ['id',]
    search_fields = ['order']
    list_filter = ['sale_date']
    