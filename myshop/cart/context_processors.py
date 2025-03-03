from .cart import Cart


def cart (request):
        return {'cart':Cart(request)}

def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user).first()
        cart_item_count = cart.items.count() if cart else 0
    else:
        cart_item_count = 0
    return {'cart_item_count': cart_item_count}
