from django.db import models
from shop.models import Products
import datetime


class Cart():
        def __init__(self,request):
                self.session = request.session
                cart = self.session.get('session_key')
                if 'session_key' not in request.session:
                        cart = self.session['session_key'] = {}
                self.cart = cart
        def add(self,product):
                product_id = str(product.id)
                if product_id in self.cart:
                        pass
                        # self.cart[product_id] = {'qty': 1, 'price': str(product.price)}
                else:
                        self.cart[product_id] = {}
                        self.save()
        def save(self):
                self.session.modified = True
        def __len__(self):
                return len(self.cart)
        def get_prods(self):
                products_id = self.cart.keys()
                products = Products.objects.filter(id__in=products_id)
                return products
