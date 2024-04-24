from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from store.models import Inventory
from store.models import Customer
from django.http import JsonResponse
from django.contrib import messages

# Create your views here.
def cart(request):
    if request.user.is_authenticated:
        user = Customer.objects.get(userID=request.user)
    cart = Cart(request)
    cart_books = cart.get_cart
    quantities = cart.get_cnt
    totals = cart.total()
    return render(request, "cart.html", {"cart_books":cart_books, "quantities": quantities, "totals": totals, 'customer': user})

def cartAdd(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        book_ISBN = int(request.POST.get('books_ISBN'))

        book = get_object_or_404(Inventory, isbn=book_ISBN)

        cart.add(book=book, quantity='1')

        response = JsonResponse({'Product Name: ': book.title})
        return response

def cartDelete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post' :

        book = int(request.POST.get('books_ISBN'))

        cart.delete(book=book)

        response = JsonResponse({'Product Name: ': book})
        return response

def cartUpdate(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        book_isbn = int(request.POST.get('books_ISBN'))
        book_cnt = int(request.POST.get('books_cnt'))

        cart.update(book=book_isbn, quantity=book_cnt)

        response = JsonResponse({'qty':book_cnt})
        return response
    
def order(request):
    if request.user.is_authenticated:
        user = Customer.objects.get(userID=request.user)
    cart = Cart(request)
    cart_books = cart.get_cart
    quantities = cart.get_cnt
    totals = cart.total()
    return render(request, "order.html", {"cart_books":cart_books, "quantities": quantities, "totals": totals, 'customer': user})

def orderPlace(request):
    order = Cart(request)
    if request.user.is_authenticated:
        current_user = Customer.objects.get(userID=request.user)
    order.placeOrder(current_user.userID)
    messages.success(request, "Your order has been placed")
    return redirect(cart)