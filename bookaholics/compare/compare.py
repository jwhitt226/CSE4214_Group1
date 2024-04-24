from store.models import Inventory

class Compare():
    def __init__(self, request):
        self.session = request.session

        compare = self.session.get('session_key')

        if 'session_key' not in request.session:
            compare = self.session['session_key'] = {}

        self.compare = compare

    def add(self, book):
        book_id = str(book.id)

        if book_id in self.compare:
            pass
        else:
            self.compare[book_id] = {'price': str(book.price)}

        self.session.modified = True

    def get_compare(self):
        book_ids = self.compare.keys()

        books = Inventory.objects.filter(id__in=book_ids)

        return books
    
    def delete(self, book):
        book_ID = str(book)

        #if book_ID in self.comaper:
        del self.compare[book_ID]
        
        self.session.modified = True