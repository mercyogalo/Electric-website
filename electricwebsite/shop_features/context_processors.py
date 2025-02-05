from .shop_features import Cart


def cart(request):
    return {'cart': Cart(request)}