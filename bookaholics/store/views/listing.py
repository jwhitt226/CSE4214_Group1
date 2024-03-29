from django.shortcuts import render
from ..models import Inventory
from django.db.models import Q

def browse(request):
    if 'q' in request.GET:
        q = request.GET['q']
        multiple_q = Q(Q(title__icontains = q) | Q(author__icontains = q) | Q(isbn__icontains = q))
        books = Inventory.objects.filter(multiple_q)
    else:
        books = Inventory.objects.all()
    return render(request, 'userPage.html', {'books': books})




def viewListing(request, pk):
    
    #Get book information from Inventory
    book = Inventory.objects.get(pk=pk)

    return render(request, 'veiw_listing.html', {'book': book})