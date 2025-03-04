from django.shortcuts import render,redirect
from . models import Products,Category
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from .forms import CustomUserForm,UserProfileForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
        products = Products.objects.all()
        return render(request,'home.html',{'products':products})

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

def signup_user(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.email = form.cleaned_data['email']
            user.save()
            messages.success(request, 'ثبت نام موفقیتآمیز بود!')
            return redirect('login_user')
    else:
        form = CustomUserForm()
    return render(request, 'signup_user.html', {'form': form})

def single_product(request,pk):
       products_detail = Products.objects.get(id=pk)
       return render(request,'single_product.html',{'products_detail':products_detail})

def product_category(request,foo):
        foo = foo.replace('-',' ')
        try:
                category = Category.objects.get(name=foo)
                products = Products.objects.filter(category=category)
                return render(request,'categorys.html',{'products':products,'category':category})
        except:
                messages.success(request,('category not exixts'))
                return redirect('home')



def update_prof(request):
        return render(request,'update_prof.html',{})

@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'اطلاعات شما با موفقیت به‌روزرسانی شد!')
            return redirect('home')
    else:
        form = UserProfileForm(instance=request.user)
    return render(request, 'update_prof.html', {'form': form})


@login_required
def profile(request):
        user = request.user
        return render(request,'profile.html',{'user':user})
