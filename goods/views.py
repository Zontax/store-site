from django.shortcuts import render

def catalog(request):
    context = {
        'title': 'Каталог',
    }
    return render(request, 'goods/catalog.html', context)

def product(request):
    context = {
        'title': 'Продукти',
    }
    return render(request, 'goods/product.html', context)