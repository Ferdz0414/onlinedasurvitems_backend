from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.navbar, name='navbar'),
    path('', views.home, name='home'),
    path('', views.shop, name='shop'),
    path('', views.cart, name='cart'),
    path('', views.blog, name='blog'),
    
]