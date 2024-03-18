from django.contrib import admin
from goods.models import Categories, Products
from main.models import TestTable

admin.site.register(TestTable)

# Автозаповнення для slug
@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}