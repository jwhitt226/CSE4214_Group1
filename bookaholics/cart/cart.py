from store.models import Inventory

class Cart():
    def __init__(self, request):
        self.session = request.session

        cart = self.session.get('sessionKey')

        if 'sessionKey' not in request.session:
            cart = self.session['sessionKey'] = {}

        self.cart = cart

    def add(self, book):
        book_isbn = str(book.isbn)

        if book_isbn in self.cart:
            pass
        else:
            self.cart[book_isbn] = {'price': str(book.price)}

        self.session.modified = True

    def get_cart(self):
        book_isbns = self.cart.keys()

        books = Inventory.objects.filter(isbn__in=book_isbns)

        return books