from email import message
from django.contrib import messages
from django.db import transaction
from django.forms import ValidationError
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from goods.models import Product
from carts.models import Cart
from orders.models import Order, OrderItem
from orders.forms import CreateOrderForm


@login_required
def create_order(request: HttpRequest):
    if request.method == 'POST':
        form = CreateOrderForm(data=request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.all()
                    
                    if cart_items.exists():
                        
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.phone_number,
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.product.quantity
                            
                            if product.quantity < quantity:
                                raise ValidationError(f'Недостатньо товарів на складі, в наявності лише - {product.quantity}')
                            
                            OrderItem.objects.create(
                                order=order,
                                product=product,
                                name=name,
                                price=price,
                                quantity=quantity,
                            )
                            product.quantity -= quantity
                            product.save()
                            
                        cart_items.delete()
                        
                        messages.success(request, 'Замовлення оформлено!')
                        return redirect('user:profile')
                    
            except Exception as ex:
                messages.success(request, str(ex))
                return redirect('cart:order')
            
    else:
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone_number': request.user.phone_number
        }
        
        form = CreateOrderForm(initial=initial)
        
    context = {
        'title': 'Оформлення замовлення',
        'form': form    
    }
        
    return render(request, 'orders/create_order.html', context=context)
        
    # page = request.GET.get('page', 1)
    # on_sale = request.GET.get('on_sale', None)
    # order_by = request.GET.get('order_by', None)
    # query = request.GET.get('q', None)
    # goods = Product.objects.all()
    # paginator = Paginator(goods, GOODS_IN_PAGE)
    # goods_in_page = paginator.page(int(page));    
  
    
