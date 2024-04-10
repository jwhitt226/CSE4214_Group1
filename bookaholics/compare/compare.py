from store.models import Inventory

class Compare():
    def __init__(self, request):
        self.session = request.session

        compare = self.session.get('session_key')

        if 'session_key' not in request.session:
            compare = self.session['session_key'] = {}

        self.compare = compare

    def add(self, book):
        book_isbn = str(book.isbn)

        if book_isbn in self.compare:
            pass
        else:
            self.compare[book_isbn] = {'price': str(book.price)}

        self.session.modified = True

    def get_compare(self):
        book_isbns = self.compare.keys()

        books = Inventory.objects.filter(isbn__in=book_isbns)

        return books
    
    def delete(self, book):
        book_ISBN = str(book)

        #if book_ISBN in self.comaper:
        del self.compare[book_ISBN]
        
        self.session.modified = True