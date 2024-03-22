from django.db import models
from django.db.models import Model, CharField, SlugField, BooleanField, TextField, ImageField, DecimalField, PositiveIntegerField, DateTimeField, ForeignKey
from django.urls import reverse

class Category(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL Slug')
    
    class Meta():
        db_table = 'goods_categories'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        
        
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self): # Посилання на товар в адмінці
        return reverse('catalog:index', kwargs={'category_slug': self.slug})


class Product(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL Slug')
    product_code = CharField(max_length=25, unique=True, blank=True, null=True, verbose_name='Код товара')
    description = TextField(max_length=1000, blank=True, null=True, verbose_name='Опис')
    meta_keywords = TextField(max_length=1000, blank=True, null=True, verbose_name='SEO ключі')
    image = ImageField(upload_to='goods_images', blank=True, null=True, verbose_name='Зображення')
    price = DecimalField(default=0.00, max_digits=10, decimal_places=2, verbose_name='Ціна')
    discount = DecimalField(default=0.00, max_digits=4, decimal_places=2, verbose_name='Знижка, %')
    quantity = PositiveIntegerField(default=0, verbose_name='На складі')
    category = ForeignKey(to=Category, on_delete=models.CASCADE, verbose_name='Категорія')
    is_active = BooleanField(default=True, verbose_name='Чи доступний')
    created_timestamp = DateTimeField(auto_now_add=True, verbose_name='Дата додавання')
    
    class Meta():
        db_table = 'goods_products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ('id',)
        
        
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self): # Посилання на товар в адмінці
        return reverse('catalog:product', kwargs={'product_slug': self.slug})


    def display_id(self): # Велике id
        return f'{self.id:05}' 
  
    
    def sell_price(self): # Ціна зі знижкою 
        if self.discount:   
            return round(self.price - self.price * (self.discount / 100), 2) 
        
        return self.price