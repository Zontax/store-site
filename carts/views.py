from statistics import quantiles
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.contrib import auth, messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from goods.models import Product
from carts.models import Cart


def cart_add(request: HttpRequest, product_slug):
    product = Product.objects.get(slug=product_slug)
    
    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()          
        else:
            Cart.objects.create(user=request.user,product=product, quantity=1)
            
    return redirect(request.META['HTTP_REFERER'])


def cart_change(request: HttpRequest, product_slug):
    return render(request, 'carts/cart.html')


def cart_remove(request: HttpRequest, cart_id):
    cart = Cart.objects.get(id=cart_id)
    cart.delete()
    
    return redirect(request.META['HTTP_REFERER'])
