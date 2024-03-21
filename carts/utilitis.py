from carts.models import Cart
from goods.models import Product


def get_user_carts(request):
    if request.user.is_authenticated:
        return Cart.objects.filter(user=request.user).order_by('-created_timestamp')