from django.utils.html import format_html
from django.contrib import admin

from goods.models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)} # автозаповнення для slug
    list_display = ['name',] # відображення по назві а не __str__()
    
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'display_image', 'category', 'price', 'discount', 'quantity', 'is_active']
    list_editable = ['discount', 'quantity', 'is_active']
    search_fields = ['name', 'description', 'meta_keywords']
    list_filter = ['quantity', 'category', 'is_active']
    fields = [
        ('name', 'slug'),
        'category',
        'description',
        'meta_keywords',
        'image',
        ('price', 'discount'),
        'quantity',
    ]
    
    def display_image(self, obj: Product):
        if obj.image:
            return format_html(f'<a href="{obj.get_absolute_url()}" title="Дивитися на сайті"><img src="{obj.image.url}" width="50" height="50" /></a>')
        return None
    
    display_image.short_description = 'Icon'
