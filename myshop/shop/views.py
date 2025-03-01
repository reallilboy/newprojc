from django.shortcuts import render
from . models import Products,Category
# Create your views here.
def home(request):
        products = Products.objects.all()
        return render(request,'index.html',{'products':products})
