from django.db import models
from django.db.models import Model, CharField, QuerySet, SlugField, DecimalField, PositiveSmallIntegerField, ForeignKey, DateTimeField
from users.models import User
from goods.models import Product


class CartQuerySet(QuerySet):
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0
    
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)


class Cart(Model):
    user = ForeignKey(to=User, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Власник корзини')
    product = ForeignKey(to=Product, on_delete=models.CASCADE, verbose_name='Товар')
    quantity = PositiveSmallIntegerField(default=0, verbose_name='Кількість')
    session_key = CharField(max_length=32, blank=True, null=True, verbose_name='Не зареєстрований (ключ сесії)')
    created_timestamp = DateTimeField(auto_now_add=True, verbose_name='Дата додавання')
    
    class Meta:
        db_table = 'carts'
        verbose_name='Корзина'
        verbose_name_plural='Корзини'
    
    objects = CartQuerySet().as_manager()

    def __str__(self):
        return f'Кошик {self.user.username} | Товар {self.product.name} | Кількість {self.quantity}'
    
    
    def products_price(self):  
        return round(self.product.sell_price() * self.quantity, 2)