from django.shortcuts import render, redirect
from store.models import Inventory, Seller, Customer, User
from django.http import JsonResponse

def adminPage(request):
    books = Inventory.objects.all()
    i_sellers = Seller.objects.filter(status='INACTIVE')
    a_sellers = Seller.objects.filter(status='ACTIVE')
    customers = User.objects.filter(type = 'CUSTOMER', is_active=True)

    return render(request, 'adminPage.html', {'books':books, 'i_sellers':i_sellers, 'a_sellers':a_sellers, 'customers':customers})

def removeBook(request):
    if request.POST.get('action') == 'post' :

        bookid = int(request.POST.get('bookid'))

        book = Inventory.objects.get(id=bookid)

        book.delete()

def deactivate(request):
    if request.POST.get('action') == 'post' :
        sellerid = int(request.POST.get('sellerid'))
        s = Seller.objects.get(sellerID_id=sellerid)
        s.status = 'INACTIVE'
        s.save()
        u = User.objects.get(id=sellerid)
        u.is_active = False
        u.save()
        i = Inventory.objects.filter(sellerID=sellerid)
        i.delete()

    return redirect('adminPage')

def activate(request):
    if request.POST.get('action') == 'post' :
        sellerid = int(request.POST.get('sellerid'))
        s = Seller.objects.get(sellerID_id=sellerid)
        s.status = 'ACTIVE'
        s.save()
        u = User.objects.get(id=sellerid)
        u.is_active = True
        u.save()

    return redirect('adminPage')

def deactivateUser(request):
    if request.POST.get('action') == 'post' :
        customerid = int(request.POST.get('customerid'))
        u = User.objects.get(id=customerid)
        u.is_active = False
        u.save()

    return redirect('adminPage')