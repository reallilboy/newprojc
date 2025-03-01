from django.contrib import admin
from . models import Products,Category,Order,Customer
# Register your models here.

admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Category)
admin.site.register(Order)
