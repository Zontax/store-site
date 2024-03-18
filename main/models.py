from django.db import models
from django.db.models import Model, CharField, SlugField, TextField, ImageField, DecimalField, PositiveIntegerField, ForeignKey


class TestTable(Model):
    name = CharField(max_length=150, unique=True, verbose_name='Назва')
    slug = SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL Slug')
    
    class Meta():
        db_table = 'test_data'
        verbose_name = 'Тестові дані'
        verbose_name_plural = 'Тестові дані'
        
    def __str__(self):
        return self.name
        