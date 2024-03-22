from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from goods.models import Product


@login_required
def create_order(request: HttpRequest):
    # page = request.GET.get('page', 1)
    # on_sale = request.GET.get('on_sale', None)
    # order_by = request.GET.get('order_by', None)
    # query = request.GET.get('q', None)
    # goods = Product.objects.all()
    # paginator = Paginator(goods, GOODS_IN_PAGE)
    # goods_in_page = paginator.page(int(page));    
    
    # context = {
    #     'title': 'Каталог',
    #     'goods': goods_in_page,
    # }
    return render(request, 'orders/create_order.html')
