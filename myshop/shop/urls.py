from django.urls import path,include
from . import views as shop_views
urlpatterns = [
        path('',shop_views.home,name='home'),
        path('login_user/',shop_views.login_user,name='login_user'),
        path('logout/',shop_views.logout_user,name='logout_user'),
]
