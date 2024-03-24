from django.core.paginator import Paginator
from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404
from goods.models import Product
from app.settings import GOODS_IN_PAGE
from goods.services import q_search


def catalog(request: HttpRequest, category_slug=None):
    page = request.GET.get('page', 1)
    on_sale = request.GET.get('on_sale', None)
    order_by = request.GET.get('order_by', None)
    query = request.GET.get('q', '')
    
    if category_slug == 'all' or query.strip() == '':
        goods = Product.objects.all()
    elif query:
        goods = q_search(query)
    else:
        goods = Product.objects.filter(category__slug=category_slug)
        
    if on_sale:
        goods = goods.filter(discount__gt=0) # фільтр по знижці більшій за нуль
        
    if order_by and order_by != 'default':
        goods = goods.order_by(order_by) # сортування
    
    paginator = Paginator(goods, GOODS_IN_PAGE)
    goods_in_page = paginator.page(int(page));    
    
    context = {
        'title': 'Каталог',
        'goods': goods_in_page,
        'slug_url': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request: HttpRequest, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'title': product.name,
        'product': product, 
    }
    return render(request, 'goods/product.html', context)
