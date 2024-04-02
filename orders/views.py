from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.db import transaction
from django.views.generic import View
from django.http import HttpRequest

from carts.models import Cart
from orders.models import Order, OrderItem
from orders.forms import CreateOrderForm
import bleach


@method_decorator(login_required, name='dispatch')
class CreateOrderView(View):
    title = 'Оформлення замовлення'
    
    def get(self, request: HttpRequest):
        initial = {
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'phone_number': request.user.phone_number
        }
        form = CreateOrderForm(initial=initial)
        
        context = {
            'title': self.title,
            'order': True,
            'form': form
        }
        return render(request, 'orders/create_order.html', context=context)


    def post(self, request):
        form = CreateOrderForm(data=request.POST)
        
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = request.user
                    cart_items = Cart.objects.all()
                    
                    if cart_items.exists():
                        order = Order.objects.create(
                            user=user,
                            phone_number=form.cleaned_data['phone_number'],
                            requires_delivery=form.cleaned_data['requires_delivery'],
                            delivery_address=form.cleaned_data['delivery_address'],
                            payment_on_get=form.cleaned_data['payment_on_get'],
                        )
                        
                        for cart_item in cart_items:
                            product = cart_item.product
                            name = cart_item.product.name
                            price = cart_item.product.sell_price()
                            quantity = cart_item.quantity
                            
                            if product.quantity < quantity:
                                messages.error(request, f'Недостатньо товарів, "{product.name}" в наявності лише - {product.quantity} шт.')
                                transaction.set_rollback(True)
                                return redirect('orders:create_order')
                            
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
                        
                        messages.success(request, 'Дякуємо за ваше замовлення! Ви можете відслідкувати статус замовлення в <a href="/user/profile/">особистому кабінеті</a>')
                        return redirect('user:profile')
                    
            except Exception as ex:
                messages.error(request, str(ex))
                transaction.set_rollback(True)
                return redirect('orders:create_order')
        
        context = {
            'title': self.title,
            'order': True,
            'form': form
        }
        return render(request, 'orders/create_order.html', context=context)
