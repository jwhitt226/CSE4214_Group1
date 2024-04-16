from django.shortcuts import render, redirect
from ..models import OrderHist
from ..models import Customer
from ..models import Inventory
from ..models import Seller
from django.http import JsonResponse

def orderReturn(request):
    if request.user.is_authenticated:
        current_user = Customer.objects.get(userID=request.user)

    id = current_user.userID

    #dict[key]=value

    orders = OrderHist.objects.filter(userID=id)
    books = {}
    for order in orders:
        
        books[order] = Inventory.objects.get(id=order.itemID)

    return render(request, 'return.html', {'books': books, 'customer':current_user})


def refund(request):
    if request.POST.get('action') == 'post' :

        orderid = int(request.POST.get('orderID'))

        order = OrderHist.objects.get(orderID=orderid)
        book = Inventory.objects.get(id=order.itemID)
        user = Customer.objects.get(userID=order.userID)
        seller = Seller.objects.get(sellerID_id=book.sellerID)

        seller.credit = seller.credit - order.price
        seller.save()
        user.credit = user.credit + order.price
        user.save()

        order.delete()

        response = JsonResponse({'user': user})
        return response
