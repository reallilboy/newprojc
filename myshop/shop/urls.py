from django.urls import path,include
from . import views as shop_views
urlpatterns = [
        path('',shop_views.home,name='home'),
        path('login_user/',shop_views.login_user,name='login_user'),
        path('logout/',shop_views.logout_user,name='logout_user'),
        path('signup_user/',shop_views.signup_user,name='signup_user'),
        path('product_detail/<int:pk>',shop_views.single_product,name='single_product'),
        path('products_category/<str:foo>',shop_views.product_category,name='products_category'),
        path('cart/',include('cart.urls'))
]
