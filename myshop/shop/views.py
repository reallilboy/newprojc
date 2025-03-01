from django.shortcuts import render,redirect
from . models import Products,Category
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages


# Create your views here.

def home(request):
        products = Products.objects.all()
        return render(request,'index.html',{'products':products})

def login_user(request):
        if request.method == 'POST':
                username = request.POST['username']
                password = request.POST['password']
                user = authenticate(request,username=username,password=password)
                if user is not None:
                        login(request,user)
                        messages.success(request,('success'))
                        return redirect('home')
                else:
                        messages.success(request,('you have error'))
                        return redirect('login_user')
        else:
                return render(request,'login_user.html')


def logout_user(request):
        logout(request)
        return redirect('home')
