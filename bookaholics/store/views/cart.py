from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from bookaholics.store.models import Inventory

class Cart(View):
    cart_items = request.session.get('cart', {})

    stock_id = list(cart_items.keys)
