from statistics import quantiles
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest, JsonResponse
from django.contrib import auth, messages
from django.template.loader import render_to_string
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from carts.utilitis import get_user_carts
from goods.models import Product
from carts.models import Cart


def cart_add(request: HttpRequest):
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
            Cart.objects.create(user=request.user,product=product, quantity=1)
    
    user_carts = get_user_carts(request)
    cart_items_html = render_to_string('carts/_included_cart.html', { 'carts': user_carts }, request=request)        
    
    responce_data =  {
        "message": "Товар додано в корзину",
        "cart_items_html": cart_items_html
    }
    return JsonResponse(responce_data)


def cart_change(request: HttpRequest):
    return render(request, 'carts/cart.html')


def cart_remove(request: HttpRequest):
    # cart = Cart.objects.get(id=cart_id)
    # cart.delete()
    
    return redirect(request.META['HTTP_REFERER'])
