from django.shortcuts import render
from ..models import Inventory
from ..models import Seller

def processaddListing(request):
    if request.method == 'POST' and request.FILES['image_name']:
        isbn = request.POST.get('isbn_name')
        title = request.POST.get('title_name')
        author = request.POST.get('author_name')
        genre = request.POST.get('genre_name')
        stock = 1
        image = request.FILES['image_name']
        price = request.POST.get('price_name')
 #       current_user = Seller.objects.get(sellerID=request.user.id)
 #       sellerID = current_user.sellerID_id
        sellerID = request.user

        listing = Inventory(isbn=isbn, title=title, author=author, genre=genre, price=price, stock=stock, image=image, sellerID=sellerID)
        listing.save()

        return render(request, 'userPage.html')
    else:
        return render(request, 'addListing.html')