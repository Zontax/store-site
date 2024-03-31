from django.db.models import Model, QuerySet, CharField, TextField, DecimalField, PositiveIntegerField, ForeignKey, DateTimeField, BooleanField
from django.db import models

from phonenumber_field.modelfields import PhoneNumberField
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
    user = ForeignKey(User, on_delete=models.SET_DEFAULT, verbose_name='Покупець', default=None, blank=True, null=True)
    created_timestamp = DateTimeField('Дата створення замовлення', auto_now_add=True)
    phone_number = PhoneNumberField('Номер телефону', region='UA', blank=True, null=True)
    requires_delivery = BooleanField('Потрібна доставка', default=False)
    delivery_address = TextField('Адреса доставки', blank=True, null=True)
    payment_on_get = BooleanField('Оплата при отриманні', default=False)
    is_paid = BooleanField('Оплачено', default=False)
    status = CharField('Статус замовлення', max_length=50, default='В обробці...')
    
    class Meta:
        db_table = 'orders'
        verbose_name='Замовлення'
        verbose_name_plural='Замовлення'
        ordering = ('-created_timestamp',)


    def __str__(self):
        return f'Замовлення № {self.pk} | Покупець: {self.user.first_name} {self.user.last_name}'

    
class OrderItem(Model):
    order = ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Замовлення')
    product = ForeignKey(Product, on_delete=models.SET_DEFAULT, verbose_name='Товар', default=None, null=True)
    delivery_address = TextField('Адреса доставки', blank=True, null=True)
    name = CharField('Назва', max_length=150)
    price = DecimalField('Назва', max_digits=10, decimal_places=2)
    quantity = PositiveIntegerField('Кількість', default=0)
    sale_date = DateTimeField('Дата продажу', auto_now_add=True)
    
    class Meta:
        db_table = 'order_items'
        verbose_name='Товар замовлення'
        verbose_name_plural='Товари замовлення'
        ordering = ('sale_date',)

    objects = OrderItemQuerySet().as_manager()


    def __str__(self):
        return f'Товар: {self.name} | Замовлення № {self.order.pk}'    
    
    
    def products_price(self):  
        return round(self.price * self.quantity, 2)
