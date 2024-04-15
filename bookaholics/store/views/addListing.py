from django.shortcuts import render
from ..models import Inventory

def processaddListing(request):
    if request.method == 'POST':
        isbn = request.POST.get('isbn_name')
        title = request.POST.get('title_name')
        author = request.POST.get('author_name')
        genre = request.POST.get('genre_name')
        stock = 1
        image = request.POST.get('image_name')
        price = request.POST.get('price_name')

        listing = Inventory(isbn=isbn, title=title, author=author, genre=genre, price=price, stock=stock, image=image)
        listing.save()

        return render(request, 'userPage.html')
    else:
        return render(request, 'addListing.html')