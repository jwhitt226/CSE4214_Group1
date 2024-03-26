from django.shortcuts import render, redirect
from bookaholics.store.models import User, Inventory, ShoppingCart
from django.views import View

class Checkout(View):
    def post(self,request):
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        user_id = request.session.get('user_id')
        user = user.objects.get(id = user_id)

        cart = request.session.get('cart')
        stock_id = list(cart.keys())
        stock = Inventory.objects.filter(id__in=stock_id)

        for stock in stock:
            quantity = cart[str(stock_id)]
            order = ShoppingCart.objects.create(
                customer = user,
                stock = stock,
                price = stock.price,
                address = address,
                phone = phone,
                quantity = quantity
            )

            request.session['cart'] = {}

            return redirect('cart')