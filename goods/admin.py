from email.mime import image
from django.contrib import admin
from goods.models import Category, Product

# admin.site.register(Category)

# Автозаповнення для slug
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name',] # відображення по назві а не __str__()
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'category', 'price', 'discount', 'quantity']
    list_editable = ['discount', 'quantity']
    search_fields = ['name', 'description']
    list_filter = ['quantity', 'category']
    fields = [
        'name',
        'category',
        'slug',
        'description',
        'image',
        ('price', 'discount'),
        'quantity',
    ]