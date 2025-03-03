from django.shortcuts import render,get_object_or_404
from . cart import Cart
from shop.models import Products
from django.http import JsonResponse



def cart_summary(request):
        return render(request,'cart_summary.html',{})


def cart_add(request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
                products_id = int(request.POST.get('product_id'))
                product = get_object_or_404(Products,id=products_id)
                cart.add(product=product)
                return JsonResponse({ 'product name': product.product_name})

def cart_delete(request):
        pass


def cart_update(request):
        pass
