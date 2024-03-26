from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from store.models import User
from django.views import View
from store.models import Inventory
from store.models import OrderHist
from store.middlewares.auth import auth_middleware

class OrderView(View):


    def get(self , request ):
        customer = request.session.get('user')
        orders = OrderHist.get_orders_by_user(User)
        print(orders)
        return render(request , 'orders.html'  , {'orders' : orders})
