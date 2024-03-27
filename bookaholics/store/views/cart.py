from urllib import request
from django.shortcuts import render, redirect
from django.views import View
from bookaholics.store.models import Inventory

class Cart(View):
    def get(self,request):
        cart_items = request.session.get('cart', {})
        stock_id = list(cart_items.keys())
        stock = Inventory.objects.filter(id__in=stock_id) 
        return render(request, 'cart.html',{'stock': stock, 'cart_items': cart_items})

    def post(self, request):
        stock_id = request.POST.get('stock_id')
        action = request.POST.get('action')
        cart_items = request.session.get('cart', {})

        if action == 'add':
            cart_items[stock_id] = cart_items.get(stock_id, 0) + 1
            stock = Inventory.objects.get(id=stock_id)
            stock.quantity -= 1
            stock.save()

        elif action == 'remove':
            if stock_id in cart_items:
             stock = Inventory.objects.get(id=stock_id)
             stock.quantity += 1
             stock.save()
            del cart_items[stock_id]

            request.session['cart'] = cart_items
            return redirect('cart')