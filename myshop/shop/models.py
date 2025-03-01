from django.db import models
import datetime
# Create your models here.


class Category(models.Model):
        name = models.CharField(max_length=30)

        def __str__(self):
                return self.name

class Products(models.Model):
        product_name = models.CharField( max_length=50)
        price = models.DecimalField( max_digits=100, decimal_places=0,default=0)
        product_image = models.ImageField(upload_to='uploads/products_iamge')
        product_name = models.CharField( max_length=50)
        is_sale = models.BooleanField(default=False)
        sale_price = models.DecimalField( max_digits=100, decimal_places=0,default=0)

        def __str__(self):
                return self.product_name

class Customer(models.Model):
        f_name = models.CharField(max_length=50)
        l_name = models.CharField(max_length=50)
        phone = models.CharField(max_length=50)
        email = models.EmailField(max_length=50)
        password= models.CharField(max_length=50)

        def __str__(self):
                return {self.f_name},{self.l_name}

class Order(models.Model):
        porduct_order = models.ForeignKey(Products,on_delete=models.CASCADE)
        customer_order = models.ForeignKey(Customer,on_delete=models.CASCADE)
        quantity = models.IntegerField(default=1)
        adders = models.CharField(max_length=40,default='',blank=True)
        date = models.DateField(default=datetime.datetime.today)
        status = models.BooleanField(default=False)

        def __str__(self):
                return self.product_name
