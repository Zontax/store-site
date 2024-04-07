from django.template.loader import render_to_string
from django.http import HttpRequest, JsonResponse
from django.views import View

from carts.services import get_user_carts
from carts.models import Cart
from goods.models import Product


class CartAddProductAPI(View):
    
    def post(self, request: HttpRequest):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        
        if request.user.is_authenticated:
            carts = Cart.objects.filter(user=request.user, product=product)
            
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(user=request.user, product=product, quantity=1)
                
        else:
            carts = Cart.objects.filter(session_key=request.session.session_key, product=product)
            
            if carts.exists():
                cart = carts.first()
                if cart:
                    cart.quantity += 1
                    cart.save()
            else:
                Cart.objects.create(session_key=request.session.session_key, product=product, quantity=1)
        
        user_carts = get_user_carts(request)
        cart_items_html = render_to_string('carts/_included_cart.html', { 'carts': user_carts }, request=request)
        
        response_data = {
            "message": f'<b>{product.name}</b> додано в кошик (<b>{carts.first().quantity}</b> шт)',
            "cart_items_html": cart_items_html
        }
        return JsonResponse(response_data)


class CartUpdateQuantityAPI(View):
    
    def post(self, request: HttpRequest):
        cart_id = request.POST.get('cart_id')
        quantity = request.POST.get('quantity')

        cart = Cart.objects.get(id=cart_id)
        cart.quantity = quantity
        cart.save()

        carts = get_user_carts(request)
        cart_items_html = render_to_string('carts/_included_cart.html', { 'carts': carts }, request=request)

        response_data = {
            "message": f'Кількість <b>{cart.product.name}</b> (<b>{quantity}</b> шт)',
            "cart_items_html": cart_items_html,
            "quantity": quantity,
        }
        return JsonResponse(response_data)


class CartRemoveProductAPI(View):
    
    def post(self, request: HttpRequest):
        cart_id = request.POST.get("cart_id")

        cart = Cart.objects.get(id=cart_id)
        quantity = cart.quantity
        cart.delete()

        user_cart = get_user_carts(request)
        cart_items_html = render_to_string(
            "carts/_included_cart.html", {"carts": user_cart}, request=request)

        response_data = {
            "message": f'<b>{cart.product.name}</b> (<b>{cart.quantity}</b> шт) видалено з кошика',
            "cart_items_html": cart_items_html,
            "quantity_deleted": quantity,
        }
        return JsonResponse(response_data)
