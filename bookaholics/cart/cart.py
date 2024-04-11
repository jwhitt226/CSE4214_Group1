from store.models import Inventory
from decimal import *

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('sessionKey')

        if 'sessionKey' not in request.session:
            cart = self.session['sessionKey'] = {}

        self.cart = cart

    def add(self, book, quantity):
        book_isbn = str(book.isbn)
        quantity = str(quantity)

        if book_isbn in self.cart:
            pass
        else:
            self.cart[book_isbn] = int(quantity)

        self.session.modified = True

    def get_cart(self):
        book_isbns = self.cart.keys()

        books = Inventory.objects.filter(isbn__in=book_isbns)

        return books
    
    def delete(self, book):
        book_ISBN = str(book)

        #if book_ISBN in self.cart:
        del self.cart[book_ISBN]
        
        self.session.modified = True

    def get_cnt(self):
        quantities = self.cart
        return quantities
    
    def update(self, book, quantity):
        book_ISBN = str(book)
        book_cnt = str(quantity)

        cart = self.cart

        cart[book_ISBN] = book_cnt

        self.session.modified = True
        
        x = self.cart
        return x
    
    def total(self):
        book_isbns = self.cart.keys()

        books = Inventory.objects.filter(isbn__in=book_isbns)

        quantities = self.cart

        ttl = 0
        for key, value in quantities.items():
            key = int(key)
            for book in books:
                if book.isbn == key:
                    ttl = ttl + ( Decimal(float(value)) * book.price)
        return ttl
    
    def placeOrder(self):
        book_isbns = self.cart.keys()

        books = Inventory.objects.filter(isbn__in=book_isbns)

        quantities = self.cart
        
        
        for key, value in list(sorted(quantities.items())):
            Inventory.objects.filter(isbn=key).update(stock=(Inventory.objects.get(isbn=key).stock - int(value)))
            del self.cart[key]
        
        self.session.modified = True


