from django.db import models
from django.db.models import Model, CharField, SlugField, TextField, ImageField, DecimalField, PositiveIntegerField, ForeignKey

class Categories(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL Slug')
    
    class Meta():
        verbose_name = 'Категорію'
        verbose_name_plural = 'Категорії'
        
    def __str__(self):
        return f'{self.name} ({self.slug})' 


class Products(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL Slug')
    description = TextField(max_length=200, blank=True, null=True, verbose_name='Опис')
    image = ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Зображення')
    price = DecimalField(default=0.00, max_digits=7, decimal_places=2, verbose_name='Ціна')
    discount = DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Знижка')
    quantity = PositiveIntegerField(default=0, verbose_name='Кількість')
    category = ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категорія')
    
    class Meta():
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукти'
        
    def __str__(self):
        return f'{self.name} ({self.slug}) - {self.quantity}' 
