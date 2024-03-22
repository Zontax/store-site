from itertools import product
from tabnanny import verbose
from django.db import models
from django.db.models import Model, QuerySet, CharField, TextField, SlugField, DecimalField, PositiveIntegerField, ForeignKey, DateTimeField, BooleanField
from phonenumber_field.modelfields import PhoneNumberField
from traitlets import default
from users.models import User
from goods.models import Product


class OrderItemQuerySet(QuerySet):
    
    def total_price(self):
        return sum(cart.products_price() for cart in self)
    
    def total_quantity(self):
        if self:
            return sum(cart.quantity for cart in self)
        return 0


class Order(Model):
    user = ForeignKey(to=User, on_delete=models.SET_DEFAULT, default=None, blank=True, null=True, verbose_name='Покупець')
    created_timestamp = DateTimeField(auto_now_add=True, verbose_name='Дата створення замовлення')
    phone_number = PhoneNumberField(region='UA', blank=True, null=True, verbose_name='Номер телефону')
    requires_delivery = BooleanField(default=False, verbose_name='Потрібна доставка')
    delivery_address = TextField( blank=True, null=True, verbose_name='Адреса доставки')
    payment_on_get = BooleanField(default=False, verbose_name='Оплата при отриманні')
    is_paid = BooleanField(default=False, verbose_name='Оплачено')
    status = CharField(max_length=50, default='В обробці...', verbose_name='Статус замовлення')
    
    class Meta:
        db_table = 'orders'
        verbose_name='Замовлення'
        verbose_name_plural='Замовлення'
        ordering = ('created_timestamp',)


    def __str__(self):
        return f'Замовлення № {self.pk} | Покупець {self.user.first_name} {self.user.last_name} ({self.user.username}) | "{self.product.name}" {self.quantity} шт'

    
    
class OrderItem(Model):
    order = ForeignKey(to=Order, on_delete=models.CASCADE, verbose_name='Замовлення')
    product = ForeignKey(to=Product, on_delete=models.SET_DEFAULT, default=None, null=True, verbose_name='Товар')
    delivery_address = TextField( blank=True, null=True, verbose_name='Адреса доставки')
    name = CharField(max_length=150, verbose_name='Назва')
    price = DecimalField(max_digits=10, decimal_places=2, verbose_name='Назва')
    quantity = PositiveIntegerField(default=0, verbose_name='Кількість' )
    sale_date = DateTimeField(auto_now_add=True, verbose_name='Дата продажу')
    
    class Meta:
        db_table = 'order_items'
        verbose_name='Проданий товар'
        verbose_name_plural='Продані товари'
        ordering = ('sale_date',)

    objects = OrderItemQuerySet().as_manager()


    def __str__(self):
        return f'Товар: {self.name} | Замовлення № {self.order.pk}'    
    
    
    def products_price(self):  
        return round(self.price * self.quantity, 2)
