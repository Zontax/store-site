from django.db.models import Model, Index, CharField, SlugField, BooleanField, TextField, ImageField, DecimalField, PositiveIntegerField, DateTimeField, ForeignKey
from django.db import models
from django.urls import reverse


class Category(Model):
    name = CharField('Назва', max_length=150, unique=True)
    slug = SlugField('URL Slug', max_length=200, unique=True, blank=True, null=True)
    
    class Meta():
        db_table = 'categories'
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        
        
    def __str__(self):
        return self.name
    
    
    def get_absolute_url(self): # Посилання на товар в адмінці
        return reverse('catalog:index', kwargs={'category_slug': self.slug})


class Product(Model):
    name = CharField('Назва', max_length=150, unique=True)
    slug = SlugField('URL Slug', max_length=200, unique=True, blank=True, null=True)
    product_code = CharField('Код товара', max_length=25, unique=True, blank=True, null=True)
    description = TextField('Опис', max_length=1000, blank=True, null=True)
    meta_keywords = CharField('Meta інформація', max_length=400, blank=True, null=True)
    image = ImageField('Зображення', upload_to='images/goods_picture', blank=True, null=True)
    price = DecimalField('Ціна', default=0.00, max_digits=10, decimal_places=2)
    discount = DecimalField('Знижка, %', default=0.00, max_digits=4, decimal_places=2)
    quantity = PositiveIntegerField('На складі', default=0)
    category = ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Категорія')
    is_active = BooleanField(default=True, verbose_name='Чи доступний')
    created_timestamp = DateTimeField('Дата додавання', auto_now_add=True)
    
    class Meta():
        db_table = 'products'
        indexes = [Index(fields=['id', 'name', 'slug', 'description', 'meta_keywords']),]
        ordering = ('-created_timestamp',)
        
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
       
        
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
    
    