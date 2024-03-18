from django.http import Http404, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from goods.models import Product

def catalog(request, category_slug):
    if category_slug == 'all':
        goods = Product.objects.all()
    else:
        goods = Product.objects.filter(category__slug=category_slug)
        if not goods.exists():
            raise Http404('Товарів для цієї категорії неіснує')
        
    context = {
        'title': 'Каталог',
        'goods': goods,
        'category_slug': category_slug
    }
    return render(request, 'goods/catalog.html', context)


def product(request, product_slug):
    product = Product.objects.get(slug=product_slug)
    context = {
        'title': 'Товар',
        'product': product, 
    }
    return render(request, 'goods/product.html', context)
