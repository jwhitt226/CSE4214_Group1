from django.urls import path
from . import views

urlpatterns = [
    path('', views.cart, name="cart"),
    path('add/', views.cartAdd, name="cartAdd"),
    path('delete/', views.cartDelete, name="cartDelete"),
    path('update/', views.cartUpdate, name="cartUpdate"),
    path('order/', views.order, name="order"),
    path('orderPlace/', views.orderPlace, name="orderPlace")
]