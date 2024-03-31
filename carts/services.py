from django.http import HttpRequest

from carts.models import Cart


def get_user_carts(request: HttpRequest):
    
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).select_related('product').order_by('-created_timestamp')
    
    if not request.session.session_key:
        request.session.create()
        
    return Cart.objects.filter(session_key=request.session.session_key).select_related('product').order_by('-created_timestamp')
