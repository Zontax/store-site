from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.core.paginator import Paginator
from django.views.generic import View, DetailView

from goods.models import Product
from goods.services import q_search
from app.settings import GOODS_IN_PAGE


class CatalogView(View):
    
    def get(self, request: HttpRequest, category_slug=None):
        page = request.GET.get('page', 1)
        query = request.GET.get('q', '')
        on_sale = request.GET.get('on_sale', None)
        order_by = request.GET.get('order_by', None)
        
        if (category_slug == 'all' and query == ''):
            goods = Product.objects.all().filter(is_active=True)
        elif query:
            goods = q_search(query).filter(is_active=True)
        else:
            goods = Product.objects.filter(category__slug=category_slug, is_active=True)
            
        if on_sale:
            goods = goods.filter(discount__gt=0, is_active=True)
            
        if order_by and order_by != 'default':
            goods = goods.order_by(order_by)
        
        paginator = Paginator(goods, GOODS_IN_PAGE)
        goods_in_page = paginator.page(int(page))
        new_discounted_goods = Product.objects.filter(discount__gt=0, is_active=True)[:4]
        
        context = {
            'title': 'Каталог',
            'goods': goods_in_page,
            'new_discounted_goods': new_discounted_goods,
            'slug_url': category_slug,
            'query': query
        }
        return render(request, 'goods/catalog.html', context)


class ProductView(DetailView):
    
    def get(self, request: HttpRequest, product_slug):
        product = get_object_or_404(Product, slug=product_slug, is_active=True)
        context = {
            'title': product.name,
            'product': product,
        }
        return render(request, 'goods/product.html', context)
