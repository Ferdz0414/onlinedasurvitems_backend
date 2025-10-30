from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.navbar, name='navbar'),
    path('', views.home, name='home'),
    path('', views.shop, name='shop'),
    
]