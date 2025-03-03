from django.shortcuts import render,get_object_or_404
from . cart import Cart
from shop.models import Products
from django.http import JsonResponse



def cart_summary(request):
        cart = Cart(request)
        cart_products = cart.get_prods
        products_qtys = cart.get_qty
        return render(request,'cart_summary.html',{'cart_products' :cart_products,'products_qtys':products_qtys})


def cart_add(request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
                products_id = int(request.POST.get('product_id'))
                products_qty = int(request.POST.get('product_quantity',1))
                product = get_object_or_404(Products,id=products_id)
                cart.add(product=product,quantity=products_qty)
                cart_quantity = cart.__len__()
                return JsonResponse({ 'qty': cart_quantity  })

def cart_delete(request):
        pass


def cart_update(request):
        pass
def cart_remove(request):
    cart = Cart(request) 
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product = get_object_or_404(Products, id=product_id)
        cart.remove(product)
        cart_quantity = cart.__len__()
        return JsonResponse({'qty': cart_quantity})
