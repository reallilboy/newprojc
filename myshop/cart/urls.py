from django.urls import path
from . import views as cart_views

urlpatterns = [
    path('',cart_views.cart_summary ,name='cart_summary'),
    path('cart_add/',cart_views.cart_add ,name='cart_add'),
    path('cart_delete/',cart_views.cart_delete ,name='cart_delete'),
    path('cart_update/',cart_views.cart_update ,name='cart_update'),
]
