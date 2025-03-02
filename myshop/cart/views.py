from django.shortcuts import render,get_object_or_404
from . cart import Cart
from shop.models import Products
from django.http import JsonResponse



# Create your views here.
def cart_summary(request):
        return render(request,'cart_summary.html',{})


def cart_add(request):
        cart = Cart(request)
        if request.POST.get('action') == 'post':
                product_id = int(request.POST.get('product_id'))
                product = get_object_or_404(Products,id=product_id)
                cart.add(product=product)
                response = JsonResponse({'product name':product.name})
                return response



def cart_delete(request):
        pass


def cart_update(request):
        pass
