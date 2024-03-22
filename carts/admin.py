from django.contrib import admin
from carts.models import Cart


class CartTabAdmin(admin.TabularInline):
    model = Cart
    fields = [
        'product', 'quantity', 'created_timestamp'
    ]
    readonly_fields = ['created_timestamp']
    extra = 1 # щоб менеджер міг додати замовлення користувачу


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ['user_display', 'product', 'quantity', 'all_price', 'created_timestamp']
    list_filter = ['created_timestamp', 'user__username']
    
    
    def user_display(self, obj: Cart):
        if obj.user:
            return str(obj.user)
        return 'Анонімний користувач'
    
    
    def all_price(self, obj: Cart):
        return f'{int(obj.product.sell_price() * obj.quantity)}'
    
    
    user_display.short_description = 'Покупець'
    all_price.short_description = 'Ціна за все'