from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Inventory
from django.http import JsonResponse

# Create your views here.
def cart(request):
    cart = Cart(request)
    cart_books = cart.get_cart
    return render(request, "cart.html", {"cart_books":cart_books})

def cartAdd(request):
    cart = Cart(request)

    if request.POST.get('action') == 'post':
        book_ISBN = int(request.POST.get('books_ISBN'))

        book = get_object_or_404(Inventory, isbn=book_ISBN)

        cart.add(book=book)

        response = JsonResponse({'Product Name: ': book.title})
        return response

def cartDelete(request):
    pass

def cartUpdate(request):
    pass