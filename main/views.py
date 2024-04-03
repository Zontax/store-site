from django.http import HttpRequest
from django.views import View
from django.shortcuts import render

from goods.models import Product


class IndexView(View):
    
    def get(self, request: HttpRequest):
        count = 3
        random_goods = Product.objects.filter(is_active=True).order_by('?')[:count]
        new_discounted_goods = Product.objects.filter(discount__gt=0, is_active=True)[:4]
        
        context = {
            'title': 'Головна',
            'goods': random_goods,
            'new_discounted_goods': new_discounted_goods,
        }
        return render(request, 'main/index.html', context)


class AboutView(View):
    
    def get(self, request: HttpRequest):
        context = {
            'title': 'Про нас',
            'description': 'Це шаблон "Магазин Меблів" (Django 4.2.11)',
        }
        return render(request, 'main/about.html', context)
