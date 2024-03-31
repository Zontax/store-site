from django.urls import path

from carts.views import CartAddProductAPI, CartUpdateQuantityAPI, CartRemoveProductAPI

app_name = 'carts'

urlpatterns = [
    path('cart-add/', CartAddProductAPI.as_view(), name='cart_add'),
    path('cart-change/', CartUpdateQuantityAPI.as_view(), name='cart_change'),
    path('cart-remove/', CartRemoveProductAPI.as_view(), name='cart_remove'),
]
