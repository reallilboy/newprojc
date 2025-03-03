from django.shortcuts import render,get_object_or_404
from . cart import Cart
from shop.models import Products
from django.http import JsonResponse



def cart_summary(request):
        cart = Cart(request)
        cart_products = cart.get_prods
        return render(request,'cart_summary.html',{'cart_products' :cart_products})


def cart_add(request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
                products_id = int(request.POST.get('product_id'))
                product = get_object_or_404(Products,id=products_id)
                cart.add(product=product)
                cart_quantity = cart.__len__()
                return JsonResponse({ 'qty': cart_quantity  })

def cart_delete(request):
        pass


def cart_update(request):
        pass
