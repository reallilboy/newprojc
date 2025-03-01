from django.urls import path,include
from . import views as shop_views
urlpatterns = [
        path('',shop_views.home,name='home')
]
