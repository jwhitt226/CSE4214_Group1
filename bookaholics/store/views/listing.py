from django.shortcuts import render
from ..models import Inventory
from ..models import User, Customer
from django.db.models import Q

def browse(request):
    if request.user.is_authenticated:
        customer = Customer.objects.get(userID=request.user)
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains = q) | Q(author__icontains = q) | Q(isbn__icontains = q) | Q(genre = q.lower()))
        books = Inventory.objects.filter(multiple_q)
    else:
        books = Inventory.objects.all()
    return render(request, 'userPage.html', {'books': books, 'customer': customer})

def viewListing(request, pk):
    if request.user.is_authenticated:
        user = User.objects.get(userID=request.user)
    
    #Get book information from Inventory
    book = Inventory.objects.get(id=pk)

    return render(request, 'veiw_listing.html', {'book': book, 'customer': user})